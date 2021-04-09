export VAULT_TOKEN=roottoken

# Enable database secret backend
vault secrets enable database

vault write database/config/exampledb-pg \
plugin_name=postgresql-database-plugin \
allowed_roles="exampledb-pg" \
connection_url="postgresql://{{username}}:{{password}}@postgres:5432/exampledb?sslmode=disable" \
username=exampledb \
password=exampledb

cat <<EOF > vault-postgres-creation.sql
CREATE ROLE "{{name}}" WITH LOGIN PASSWORD '{{password}}' VALID UNTIL '{{expiration}}';
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO "{{name}}";
GRANT USAGE, SELECT, UPDATE ON ALL SEQUENCES IN SCHEMA public to "{{name}}";
EOF

vault write database/roles/exampledb-pg \
db_name=exampledb-pg \
creation_statements=@vault-postgres-creation.sql \
default_ttl="5m" \
max_ttl="5m"

# Give AppRole permissions to get database credentials
cat <<EOF > ro_policy.hcl
path "database/creds/exampledb-pg" {
  capabilities = ["read"]
}
EOF
vault policy write exampledb_ra ro_policy.hcl

# Test reading credentials
vault read database/creds/exampledb-pg

# Enable AppRole
vault auth enable approle
vault write auth/approle/role/exampledb role_id=exampledb policies=exampledb_ra secret_id_ttl=0 token_num_uses=0

# Read AppRole Credentials
vault read auth/approle/role/exampledb/role-id
vault write -f auth/approle/role/exampledb/secret-id