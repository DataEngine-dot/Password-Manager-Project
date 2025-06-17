import json


def creatingSecret(sm_client,name,userid,password):
    # creates a secret 
    secretValue = {
        "userid": userid,
        "password": password
    }
    secretString = json.dumps(secretValue)
    return sm_client.create_secret(Name=name,SecretString=secretString)


if __name__ == "__main__":
    pass