import imaplib
import email
from rsa_encryption import decrypt_with_rsa  
import base64  

def receive_email(email_user, email_pass, private_key):
    mail = imaplib.IMAP4_SSL("imap.example.com")
    mail.login(email_user, email_pass)
    mail.select("inbox")

    status, data = mail.search(None, "ALL")
    mail_ids = data[0].split()

    emails = []
    for num in mail_ids:
        status, data = mail.fetch(num, "(RFC822)")
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True)
                    
                    body_bytes = base64.b64decode(body)
                    decrypted_body = decrypt_with_rsa(body_bytes, private_key)
                    emails.append(decrypted_body.decode('utf-8'))
        else:
            body = msg.get_payload(decode=True)
            
            body_bytes = base64.b64decode(body)
            decrypted_body = decrypt_with_rsa(body_bytes, private_key)
            emails.append(decrypted_body.decode('utf-8'))

    mail.logout()
    return emails
