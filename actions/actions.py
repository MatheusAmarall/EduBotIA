# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Coroutine, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

ALLOWED_TIPO_MATERIAL = (
   
    'maternal', 'pre-escola',
)

class AskTipoMaterialAction(Action):
    def name(self) -> Text:
        return "action_ask_tipo_material"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Coroutine[Any, Any, List[Dict[str, Any]]]:
        dispatcher.utter_message(response="utter_ask_tipo_material", buttons=[{"title": tipo,"payload": tipo} for tipo in ALLOWED_TIPO_MATERIAL])
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
        dispatcher.utter_message(text=f"coletei o dado {tracker.get_slot('tipo_material')}")
        tipo_lista = tracker.get_slot('tipo_material')
        print(tipo_lista)
        print(type(tipo_lista))
        if tipo_lista == 'maternal':
            dispatcher.utter_message(response='utter_material_maternal')
            
        elif tipo_lista == 'pre-escola':
            dispatcher.utter_message(response='utter_lista_material_pre')
        
        
        return [] 
        

#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
