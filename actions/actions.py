from typing import Any, Coroutine, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction, UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from utils.utils import send_email
from services.gateway_service import GatewayService

ALLOWED_TURMA = (
   
    'maternal', 'pre-escola',
)
ALLOWED_CARDAPIO = (
   
    'cardápio maternal', 'cardápio pré-escola',
)
ALLOWED_VISITANTE = (
   
    'Cardápio', 'Matricula',
    'Lista de Espera', 'Lista de Materiais','Encaminhamento'
)
ALLOWED_ENCAMINHAMENTO = (
   
    'SIM', 'NÃO'
)


##############MATERIAL
class AskTipoMaterialAction(Action):
    def name(self) -> Text:
        return "action_ask_tipo_material"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Coroutine[Any, Any, List[Dict[str, Any]]]:
        dispatcher.utter_message(response="utter_ask_tipo_material", buttons=[{"title": tipo,"payload": tipo} for tipo in ALLOWED_TURMA])
        return []
    
class SubmitFormTipoMaterial(Action):
    def name(self) -> Text:
        return 'action_submit_form_tipo_material'
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Coroutine[Any, Any, List[Dict[Text, Any]]]:
        dispatcher.utter_message(text='form enviado')

        return []
    
class MostrarListaMaterial(Action):
    def name(self) -> Text:
        return "action_mostrar_lista_material"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Coroutine[Any, Any, List[Dict[Text, Any]]]:
        tipo_lista = tracker.get_slot('tipo_material')
        if tipo_lista == 'maternal':
            dispatcher.utter_message(response='utter_material_maternal')

        elif tipo_lista == 'pre-escola':
            dispatcher.utter_message(response='utter_lista_material_pre')

        return [SlotSet('tipo_material', None)]


##############CARDAPIO
class AskTipoCardapioAction(Action):
    def name(self) -> Text:
        return "action_ask_tipo_cardapio"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Coroutine[Any, Any, List[Dict[str, Any]]]:
        dispatcher.utter_message(response="utter_ask_tipo_cardapio", buttons=[{"title": tipo,"payload": tipo} for tipo in ALLOWED_CARDAPIO])
        return []
    
class SubmitFormTipoCardapio(Action):
    def name(self) -> Text:
        return 'action_submit_form_tipo_cardapio'
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Coroutine[Any, Any, List[Dict[Text, Any]]]:
        dispatcher.utter_message(text='form enviado')

        return []
    
class MostrarCardapio(Action):
    def name(self) -> Text:
        return "action_mostrar_cardapio"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Coroutine[Any, Any, List[Dict[Text, Any]]]:
        tipo_lista = tracker.get_slot('tipo_cardapio')
        if tipo_lista == 'cardápio maternal':
            dispatcher.utter_message(response="utter_cardapio_maternal")  

        elif tipo_lista == 'cardápio pré-escola':
            dispatcher.utter_message(response="utter_cardapio_pre_escola")

        dispatcher.utter_message(response='utter_cardapio')

        return [SlotSet('tipo_cardapio', None)]
    
##########ENCAMINHAMENTO
class AskTipoEncaminhamentoAction(Action):
    def name(self) -> Text:
        return "action_ask_tipo_encaminhamento"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Coroutine[Any, Any, List[Dict[str, Any]]]:
        dispatcher.utter_message(response="utter_ask_encaminhamento", buttons=[{"title": tipo,"payload": tipo} for tipo in ALLOWED_ENCAMINHAMENTO])
        return []

class SubmitFormTipoEncaminhamento(Action):
    def name(self) -> Text:
        return 'action_submit_form_tipo_encaminhamento'

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Coroutine[Any, Any, List[Dict[Text, Any]]]:
        dispatcher.utter_message(text='form enviado')

        return []

class MostrarEncaminhamento(Action):
    def name(self) -> Text:
        return "action_mostrar_encaminhamento"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Coroutine[Any, Any, List[Dict[Text, Any]]]:
        tipo_lista = tracker.get_slot('tipo_encaminhamento')
        user_email = tracker.sender_id

        if tipo_lista == 'SIM':
            gateway_service = GatewayService()
            
            res = gateway_service.realiza_agendamento(user_email)
            match res.status_code:
                case 500 | 400 | 401 | 403:
                    errors = res.json().get('errors', [])
                    error_message = errors[0] if errors else 'Infelizmente houve um erro, tente novamente. :('
                    dispatcher.utter_message(f'{error_message}')
                case 200:
                    dispatcher.utter_message(response="utter_encaminhamento")
                    json = res.json()
                    send_email(user_email, json['dataAgendamento'])
                case _:
                    dispatcher.utter_message('Infelizmente houve um erro, tente novamente. :(')

        elif tipo_lista == 'NÃO':
            dispatcher.utter_message(response="utter_ask_encaminhamento_cancelado")

        return [SlotSet('tipo_encaminhamento', None)]


##############VISITANTE
class AskTipoVisitanteAction(Action):
    def name(self) -> Text:
        return "action_ask_tipo_visitante"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Coroutine[Any, Any, List[Dict[str, Any]]]:
        dispatcher.utter_message(response="utter_ask_tipo_visitante", buttons=[{"title": tipo,"payload": tipo} for tipo in ALLOWED_VISITANTE])
        return []
    
class SubmitFormTipoVisitante(Action):
    def name(self) -> Text:
        return 'action_submit_form_tipo_visitante'
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Coroutine[Any, Any, List[Dict[Text, Any]]]:
        dispatcher.utter_message(text='form enviado')

        return []
    
class MostrarVisitante(Action):
    def name(self) -> Text:
        return "action_mostrar_escolha_visitante"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Coroutine[Any, Any, List[Dict[Text, Any]]]:
        tipo_lista = tracker.get_slot('tipo_visitante')
        if tipo_lista == 'Cardápio':
            return[FollowupAction('tipo_cardapio_form'), SlotSet('tipo_visitante', None)]
        
        elif tipo_lista == 'Matricula':
            dispatcher.utter_message(response='utter_matricula')
 
        elif tipo_lista == 'Lista de Espera':
            dispatcher.utter_message(response='utter_lista_espera')
        
        elif tipo_lista == 'Lista de Materiais':
            return[FollowupAction('tipo_material_form'), SlotSet('tipo_visitante', None)]
        
        elif tipo_lista == 'Encaminhamento':
            return[FollowupAction('tipo_encaminhamento_form'), SlotSet('tipo_visitante', None)]

        return [SlotSet('tipo_visitante', None), SlotSet('tipo_cardapio', None), SlotSet('tipo_material', None), SlotSet('tipo_encaminhamento', None)]


class ActionDefaultFallback(Action):

# """Executes the fallback action and goes back to the previous state
# of the dialogue"""

    def name(self) -> Text:
        return "ACTION_DEFAULT_FALLBACK_NAME"
    

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="my_custom_fallback_template")

        # Revert user message which led to fallback.
        return UserUtteranceReverted()
    


