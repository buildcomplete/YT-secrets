from pickle import FALSE
from signal import SIG_DFL
import unittest
import code.SecretRepo as Repo
import code.SecretExceptions as SecretExceptions

class test_SecretRepo(unittest.TestCase):

    def test_repo_store_and_get_secret(self):
        theSecret = "hello from test"
        secretId = Repo.Store(theSecret)
        retrievedSecret = Repo.Retrieve(secretId)
        assert retrievedSecret == theSecret

    def test_repo_cannot_retrieve_non_stored_secret(self):
        self.assertRaises(
            SecretExceptions.MissingSecretException, 
            Repo.Retrieve,
            "no-such-secret")
    
    def test_repo_cannot_retrieve_more_than_once(self):
        secretId = Repo.Store("new secret")
        Repo.Retrieve(secretId)
        self.assertRaises(
            SecretExceptions.MissingSecretException,
            Repo.Retrieve,
            secretId)
