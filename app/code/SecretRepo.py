import uuid
import os
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken
import code.SecretExceptions as SecretExceptions

def filenameFromUniqueId(id):
    return f"/storage/secrets/{id}.txt"

def Store(secret):
    secretId =str(uuid.uuid4())
    key = Fernet.generate_key()
    fer = Fernet(key)
    with open(filenameFromUniqueId(secretId), 'wb') as f:
        f.write(fer.encrypt(bytes(secret, "utf-8")))
    return (secretId, key)

def DeleteSecret(secretId):
    os.remove(
        filenameFromUniqueId(secretId))

def SecretExists(secretId):
    return os.path.exists(
        filenameFromUniqueId(secretId))

def Retrieve(secretId, key):
    if not SecretExists(secretId):
        raise SecretExceptions.MissingSecretException()
    
    try:
        fer = Fernet(key)
    except ValueError:
        raise SecretExceptions.InvalidKeyException()
    
    try:
        with open(filenameFromUniqueId(secretId)) as f:
            secret = fer.decrypt(f.read()).decode()
    except InvalidToken:
        raise SecretExceptions.KeyMismatchException()
        
    DeleteSecret(secretId)
    return secret
