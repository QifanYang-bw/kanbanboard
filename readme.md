# Kanban Board

## Github repo (Still updating!)

https://github.com/QifanYang-bw/kanbanboard

## Execution

### Run the code with:
```
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
python3 app.py
```
* Existing users (Feel free to register more):
  * Username: admin, Password: admin
  * Username: zitong, Password: 123456

### Conduct unittest with:
```
python3 -m unittest discover
```

## Description

A nice Kanban Board Server + Client application using Flask + SQLAlchemy + JQuery with AJAX. General Features include:

- Add/Move/Delete Tasks
- User Login/Register/Logout 

## Highlights

- Task Drag-and-Drop feature!
- Separate Task Record for Each User
- Saved data regardless of the state of client
- Encrypted Password Record in Server
- Fancy CSS Design

---

# Session 13_1

Preclass work:

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
