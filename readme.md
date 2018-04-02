# Session 13_1

## Init
```
docker swarm init
docker stack deploy -c web/docker-compose.yml cs162-swarm
echo "Deploy Completed."
python tests.py
docker stack rm cs162-swarm
docker swarm leave --force
```
## Running
```
results = {}
API_ENDPOINT = "http://127.0.0.1:5000/add"
valid_test_exp = "12 + 3"
data = {'expression': valid_test_exp}

respons = r.post(url = API_ENDPOINT, data = data)

print('-' * 25)
print("\n Result of test")
print(respons.status_code, respons.reason)
```

# Kanban Board

Github repo:
https://github.com/QifanYang-bw/kanbanboard
