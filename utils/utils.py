import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

def send_email(email, dataAgendamento):
    EMAIL = os.getenv('EMAIL')
    PASSWORD = os.getenv('PASSWORD')

    msg = EmailMessage()

    msg['Subject'] = "Agendamento de visita com o coordenador"
    msg['From'] = EMAIL
    msg['To'] = email

    msg.set_content(f"Você tem um agendamento de visita com o coordenador para o dia {dataAgendamento}\n\nAtt,\nEduBot")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(msg)