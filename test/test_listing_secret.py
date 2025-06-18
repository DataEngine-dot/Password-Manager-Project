import pytest
import json
from src.ult import listingSecrets
from unittest.mock import Mock
from botocore.exceptions import ClientError


class TestRetrieveSecret():
    def test_listing_secrets(self):
        sm_client = Mock()

        sm_client.list_secrets.return_value ={
            "SecretList":[
                {"Name": "secret1"},
                {"Name":"secret2"}
            ]
        }

        result = listingSecrets(sm_client)

        assert result == ["secret1", "secret2"]
        sm_client.list_secrets.assert_called_once()


    def test_listing_secrets_errors(self, capfd):
        sm_client = Mock()
        error_response = {
            "Error": {
                "Code": "AccessDeniedException",
                "Message": "You do not have access"
            }
        }
        sm_client.list_secrets.side_effect = ClientError(error_response, "ListSecrets")

        result = listingSecrets(sm_client)

        out, _ = capfd.readouterr()
        assert "Failed to list secrets" in out
        assert result == []