from email.message import EmailMessage
from email.headerregistry import Address



def build_email(name_client):
    email_message = EmailMessage()
    email_message["Subject"] = "Registro de Bienvenida"
    email_message["From"] = Address(username="jairo", domain="eceleris.com", display_name="Jairo Andres")
    email_message["To"] = Address(username="destino", domain="gmail.com", display_name="Destino")
    email_message.set_content(f"Bienvenido a nuestra pagina {name_client}")
    send_email(email_message=email_message)
   

def send_email(email_message:EmailMessage):
    client = boto3.client("sesv2")
    response = client.send_email(
        FromEmailAddress="jairo@eceleris.com",
            Destination={
                "ToAddresses": ["destino@gmail.com"],
                
            },
            Content={"Raw": {"Data": email_message.as_string()}},
    )

build_email("Jairo")