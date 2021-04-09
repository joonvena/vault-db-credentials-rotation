from fastapi import FastAPI
import os
import requests

app = FastAPI()

role_id = os.getenv("APPROLE_ID", "")
role_secret = os.getenv("APPROLE_SECRET_ID", "")
vault_addr = os.getenv("VAULT_ADDR", "localhost:8200")

@app.get("/")
async def root():
    vault_token = requests.post(f"http://{vault_addr}/v1/auth/approle/login", {"role_id": role_id, "secret_id": role_secret})
    response = vault_token.json()
    print(response["auth"]["client_token"])
    token = response["auth"]["client_token"]
    db_credentials = requests.get(f"http://{vault_addr}/v1/database/creds/exampledb-pg", headers={'X-Vault-Token': token})
    print(db_credentials.text)
    return {"message": "Hello World"}
