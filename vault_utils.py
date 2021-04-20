from typing import Tuple
import requests


def login_to_vault(vault_addr: str, role_id: str, role_secret: str) -> str:
    vault_token = requests.post(
        f"http://{vault_addr}/v1/auth/approle/login",
        {"role_id": role_id, "secret_id": role_secret}
    )
    response = vault_token.json()
    return response["auth"]["client_token"]


def get_db_credentials(vault_addr: str, token: str) -> Tuple[str, str]:
    db_credentials = requests.get(
        f"http://{vault_addr}/v1/database/creds/exampledb-pg",
        headers={'X-Vault-Token': token})
    response = db_credentials.json()
    username = response["data"]["username"]
    password = response["data"]["password"]
    return username, password
