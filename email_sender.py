import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from rsa_encryption import encrypt_with_rsa

def send_email(sender_email, receiver_email, subject, body, public_key):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    encrypted_body = encrypt_with_rsa(body.encode('utf-8'), public_key)  # Ensure the body is encoded to bytes
    msg.attach(MIMEText(encrypted_body.decode('latin1'), 'plain'))  # Use a suitable encoding for the byte data

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login(sender_email, 'your_password')
        server.sendmail(sender_email, receiver_email, msg.as_string())
