from ult import listingSecrets, creatingSecret, deleteSecrets, retrieveSecret
import boto3


sm_client = boto3.client('secretsmanager')
if __name__ == "__main__":
        while True:
            action = input("Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it:\n> ").lower()
            if action == "x":
                print("Thank you. Goodbye.")
                break
            elif action == "e":
                secretIdentifier = input("Secret Identifier: ")
                userId = input("UserId: ")
                password = input("Password: ")
                response = creatingSecret(sm_client,secretIdentifier,userId,password)
                print("Secret saved.")
            elif action == "r":
                recieve = input("> Specify secret to retrieve:\n> ")
                try:
                    retrieveSecret(sm_client,recieve)
                except Exception as err:
                    print(f"Oops, something went wrong: {err}")
            elif action == "d":
                toDelete = input("> Specify secret to delete:\n> ")
                try:
                    deleteSecrets(sm_client,toDelete)
                    print(f">secret {toDelete} is deleted")
                except Exception as err:
                    print(f"oops, something went wrong: {err}")
            elif action == "l":
                secrets = listingSecrets(sm_client)
                print(f"{len(secrets)} available")
                if len(secrets) > 0:
                    for secret in secrets:
                        print(f"- {secret}")
            else:
                print("invalid, please try again")