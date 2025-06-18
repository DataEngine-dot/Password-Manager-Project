import pytest
import json
from src.ult import retrieveSecret
from unittest.mock import Mock, mock_open, patch
from botocore.exceptions import ClientError


class TestRetrieveSecret():
    def retrieveSecret(self,capfd):
        sm_client = Mock()
        title = "my-secret"
        secret_data = {"userid": "admin", "password": "1234"}
        sm_client.get_secret_value.return_value = {
            "SecretString": json.dumps(secret_data)
        }

        with patch("builtins.open", mock_open()) as mocked_file:
            retrieveSecret(sm_client, title)

            sm_client.get_secret_value.assert_called_once_with(SecretId=title)
            mocked_file().write.assert_called()  
            out, _ = capfd.readouterr()
            assert "secrets is stored in secrets.json" in out
    

    def test_retrieve_secret_client_error(self, capfd):
        sm_client = Mock()
        sm_client.get_secret_value.side_effect = ClientError(
            {"Error": {"Code": "ResourceNotFoundException", "Message": "Secret not found"}},
            "GetSecretValue"
        )

        retrieveSecret(sm_client, "invalid-secret")
        out, _ = capfd.readouterr()
        assert "Failed to retrieve secret" in out


    def test_retrieve_secret_invalid_json(self, capfd):
        sm_client = Mock()
        sm_client.get_secret_value.return_value = {
            "SecretString": "not-a-valid-json"
        }

        retrieveSecret(sm_client, "bad-json-secret")
        out, _ = capfd.readouterr()
        assert "Invalid secret format" in out


    def test_retrieve_secret_unexpected_error(self, capfd):
        sm_client = Mock()
        sm_client.get_secret_value.side_effect = Exception("Something went wrong")

        retrieveSecret(sm_client, "any")
        out, _ = capfd.readouterr()
        assert "Unexpected error" in out