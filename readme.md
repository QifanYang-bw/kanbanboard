Session 13_1 Preclass Work:

```
docker swarm init
docker stack deploy -c web/docker-compose.yml cs162-swarm
echo "Sleeping now for 5s"
sleep 5
python tests.py
docker stack rm cs162-swarm
docker swarm leave --force
```
```
docker swarm init;docker stack deploy -c web/docker-compose.yml cs162-swarm;cat "Sleeping now";sleep 5s;python tests.py;docker stack rm cs162-swarm;docker swarm leave --force
```


# Kanban Board

Github repo:
https://github.com/QifanYang-bw/kanbanboard
