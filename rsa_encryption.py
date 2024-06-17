from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

def rsa_encrypt(message, public_key):
    if isinstance(message, str):
        message = message.encode('utf-8')  # Mesajı baytlara dönüştür
    ciphertext = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

def rsa_decrypt(ciphertext, private_key):
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode('utf-8')  # Baytları tekrar stringe dönüştür

def encrypt_with_rsa(message, public_key):
    return rsa_encrypt(message, public_key)

def decrypt_with_rsa(ciphertext, private_key):
    return rsa_decrypt(ciphertext, private_key)
