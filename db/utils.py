import os
from typing import Tuple

from vault_utils import login_to_vault, get_db_credentials


vault_addr = os.getenv("VAULT_ADDR", "localhost:8200")
role_id = os.getenv("APPROLE_ID", "")
role_secret = os.getenv("APPROLE_SECRET_ID", "")


def set_db_credentials() -> Tuple[str, str]:
    vault_token = login_to_vault(vault_addr, role_id, role_secret)
    return get_db_credentials(vault_addr, vault_token)
