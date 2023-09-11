from pickle import FALSE
from signal import SIG_DFL
import unittest
import code.SecretRepo as Repo
import code.SecretExceptions as SecretExceptions

class test_SecretRepo(unittest.TestCase):

    def test_repo_store_and_get_secret(self):
        theSecret = "hello from test"
        (secretId, key) = Repo.Store(theSecret)
        retrievedSecret = Repo.Retrieve(secretId, key)
        assert retrievedSecret == theSecret

    def test_repo_cannot_retrieve_non_stored_secret(self):
        self.assertRaises(
            SecretExceptions.MissingSecretException, 
            Repo.Retrieve,
            "no-such-secret",
            "no-such-key")
    
    def test_repo_cannot_retrieve_more_than_once(self):
        (secretId, key) = Repo.Store("new secret")
        Repo.Retrieve(secretId, key)
        self.assertRaises(
            SecretExceptions.MissingSecretException,
            Repo.Retrieve,
            secretId,
            key)


    def test_repo_cannot_retrieve_with_invalid_key(self):
        (secretId, key) = Repo.Store("new secret")
        self.assertRaises(
            SecretExceptions.InvalidKeyException,
            Repo.Retrieve,
            secretId,
            "pling")

    def test_repo_cannot_retrieve_with_wrong_key(self):
        (secretId, key) = Repo.Store("new secret")
        (secretId2, key2) = Repo.Store("new secret")
        self.assertRaises(
            SecretExceptions.KeyMismatchException,
            Repo.Retrieve,
            secretId,
            key2)
