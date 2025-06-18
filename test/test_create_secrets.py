import pytest
import json
from src.ult import creatingSecret
from unittest.mock import Mock



class TestCreateSecret():
    def test_creating_secrets(self):
        sm_client = Mock()
        name = "test-secret"
        userid = "testUser"
        password = "testpassword"

        expected_result = json.dumps({"userid": userid, "password": password})

        sm_client.create_secret.return_value = {"ARN": "arn:aws:secretsmanager:xyz"}

        response = creatingSecret(sm_client,name, userid,password)

        sm_client.create_secret.assert_called_once_with(Name=name, SecretString=expected_result)

        assert response["ARN"] == "arn:aws:secretsmanager:xyz"