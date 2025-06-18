from src.ult import deleteSecrets
from unittest.mock import Mock, mock_open, patch
import botocore.exceptions



class TestDeleteSecrets():
    def test_delete_secrets(self):
        sm_client = Mock()

        title = "deleteTest"

        sm_client.delete_secret.return_value = {
            "ResponseMetadata": {
                    "HTTPStatusCode": 200
                },
            "Name": title,
            "DeletionDate": "2025-06-19T12:00:00Z"
            }
        

        result = deleteSecrets(sm_client, title)

        sm_client.delete_secret.assert_called_once_with(SecretId=title)
        assert result["Name"] == title
        assert result["ResponseMetadata"]["HTTPStatusCode"] == 200
    

    def test_delete_secrets_error(self, capsys):
        sm_client = Mock()
        title = "deleteTest"

        sm_client.delete_secret.side_effect = botocore.exceptions.ClientError(
            error_response={"Error": {"Code": "ResourceNotFoundException", "Message": "Secret not found"}},
            operation_name="DeleteSecret"
        )

        result = deleteSecrets(sm_client, title)

        out, _ = capsys.readouterr()
        assert "failed to delete secret" in out.lower()
        assert result is None
