import flask_unittest
import flask.globals
import code.SecretController as Controller

class test_SecretController(flask_unittest.ClientTestCase):
    app = Controller.app
    def test_enter_secret_has_input(self, client):
        # Somehow test that the is a text input in the response...
        response = client.get('/')
        assert response.status_code == 200
        self.assertIn('secret', response.text)
