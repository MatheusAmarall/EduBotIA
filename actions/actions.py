from typing import Any, Coroutine, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

ALLOWED_TURMA = (
   
    'maternal', 'pre-escola',
)
ALLOWED_CARDAPIO = (
   
    'cardápio maternal', 'cardápio pré-escola',
)
ALLOWED_VISITANTE = (
   
    'Cardápio', 'Matricula',
    'Lista de Espera', 'Lista de Materiais',
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
            dispatcher.utter_message(text=f"Você selecionou maternal")
            dispatcher.utter_message(response='utter_material_maternal')

        elif tipo_lista == 'pre-escola':
            dispatcher.utter_message(text=f"Você selecionou pré-escola")
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
            dispatcher.utter_message(text=f"Você selecionou cardápio do maternal")  

        elif tipo_lista == 'cardápio pré-escola':
            dispatcher.utter_message(text=f"Você selecionou cardápio da pré-escola")

        dispatcher.utter_message(response='utter_cardapio')

        return [SlotSet('tipo_cardapio', None)]



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
            dispatcher.utter_message(text=f"Você selecionou cardápio")  
            dispatcher.utter_message(response='utter_ask_tipo_cardapio',buttons=[{"title": tipo,"payload": tipo} for tipo in ALLOWED_CARDAPIO])
            
            tracker.get_slot('tipo_cardapio')
        
        elif tipo_lista == 'Matricula':
            dispatcher.utter_message(text=f"Você selecionou Matricula")
 
        elif tipo_lista == 'Lista de Espera':
            dispatcher.utter_message(text=f"Você selecionou Lista de espera")
        
        elif tipo_lista == 'Lista de Materiais':
            dispatcher.utter_message(text=f"Você selecionou Lista de materiais")
            dispatcher.utter_message(response='utter_ask_tipo_cardapio',buttons=[{"title": tipo,"payload": tipo} for tipo in ALLOWED_TURMA])

        return [SlotSet('tipo_visitante', None), SlotSet('tipo_cardapio', None), SlotSet('tipo_material', None)]




