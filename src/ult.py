import json
import botocore.exceptions


def creatingSecret(sm_client,name,userid,password):
    # creates a secret 
    secretValue = {
        "userid": userid,
        "password": password
    }
    secretString = json.dumps(secretValue)
    return sm_client.create_secret(Name=name,SecretString=secretString)


def retrieveSecret(sm_client,title):
    #given a title, returns the username and password into a json file
    try:
        response = sm_client.get_secret_value(SecretId=title)
        passwords = json.loads(response["SecretString"])
        with open("secrets.json", "w") as file:
            json.dump(passwords,file,indent=4)

        print(f"secrets is stored in secrets.json")

    except botocore.exceptions.ClientError as err:
        print(f"Failed to retrieve secret: {err}")
    except (json.JSONDecodeError, KeyError) as err:
        print(f"Invalid secret format: {err}")
    except Exception as err:
        print(f"Unexpected error: {err}")


def deleteSecrets(sm_client,title):
    # deletes the secret 
    try:
        return sm_client.delete_secret(SecretId=title)

    except botocore.exceptions.clientError as err:
        print(f"failed to delete secret: {err}")
        return None


if __name__ == "__main__":
    pass