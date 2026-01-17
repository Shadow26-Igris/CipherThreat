import random
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from app.config import Config

def generate_reset_token():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(30))

def send_reset_email(email, reset_token):
    from_email = Config.FROM_EMAIL
    to_email = email
    subject = 'Password Reset Request'
    body = f'Click on the following link to reset your password: \n\n' \
           f'http://localhost:5000/reset_password/{reset_token}'

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_email, Config.EMAIL_PASSWORD)
        server.sendmail(from_email, to_email, msg.as_string())
