# Setup
Bring the stack up with docker-compose:
```
docker-compose up -d
```

Execute setup script inside the Vault container:
```
docker exec -i vault sh < setup.sh
```

If it finished successfully you should get temporary db credentials outputted to you.