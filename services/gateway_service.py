import os
import requests
from dotenv import load_dotenv

load_dotenv()

BFF_URL = os.getenv('BFF_URL')

class GatewayService:
    def realiza_agendamento(self, email):
        res = requests.post(f'{BFF_URL}/api/Agendamento/RealizaAgendamento?email={email}', headers={
            'Accept': 'application/json'
        }, verify=False)

        return res