# Session 13_1

## Init
```
docker swarm init
docker stack deploy -c web/docker-compose.yml cs162-swarm
echo "Deploy Completed."
sleep 2
python tests.py
docker stack rm cs162-swarm
docker swarm leave --force
```
## Running
```
results = {}
API_ENDPOINT = "http://127.0.0.1:5000/add"

valid_test_exp = "1 + 1"
data = {'expression': valid_test_exp}

resp_test1 = r.post(url = API_ENDPOINT, data = data)

print("\n\n Result of test 1")
print(resp_test1.status_code, resp_test1.reason)
try:
    if resp_test1.status_code == 200:
        results['test1'] = "PASS"
    else:
        results['test1'] = "FAIL"
        raise Exception('Test 1 Failed: Valid POST request')
except Exception as e:
print(e)
sys.exit(0)
```

# Kanban Board

Github repo:
https://github.com/QifanYang-bw/kanbanboard
