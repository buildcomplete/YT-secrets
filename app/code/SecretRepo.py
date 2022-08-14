import uuid
import os
import code.SecretExceptions as SecretExceptions

def filenameFromUniqueId(id):
    return "/storage/secrets/{}.txt".format(id)

def Store(secret):
    secretId =str(uuid.uuid4())
    with open(filenameFromUniqueId(secretId), 'a') as f:
        f.write(secret)
    return secretId

def DeleteSecret(secretId):
    os.remove(
        filenameFromUniqueId(secretId))

def SecretExists(secretId):
    filename = filenameFromUniqueId(secretId)
    return os.path.exists(filename)

def Retrieve(secretId):
    if not SecretExists(secretId):
        raise SecretExceptions.MissingSecretException()

    with open(filenameFromUniqueId(secretId)) as f:
        secret = f.read()
    DeleteSecret(secretId)
    return secret
    