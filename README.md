# Setup
Bring the stack up with docker-compose:
```
docker-compose up -d
```

Execute setup script inside the Vault container:
```
docker exec -i vault sh < setup.sh
```

If it finished successfully you should get DB and AppRole credentials outputted. Copy the `secret_id` value from  the output and replace the default value of `APPROLE_SECRET_ID` with copied value in docker-compose.yml. After that run `docker-compose up -d` again and application should be available in http://localhost:8000. If you want to insert some test data run `setup.sh` locally.