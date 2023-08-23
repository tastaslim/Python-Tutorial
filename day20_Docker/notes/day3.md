## Docker Commands ## 

- **docker container create 'container-name'**: This command creates a container and returns a hash string (id of
  container).
- **docker container start 'container-id'**: This command starts the container.
- **docker container run 'container-name'**: This command runs the container. If it doesn't find container in local it
  will fetch it from docker-hub
- docker run is a combination of two commands  (docker create + docker start)

```
 docker run hello-world === docker create hello-world + docker start 'container id which you get when you create a container'
```

[Docker Run](../images/docker.drawio)

- What if we just want to download docker container and not run it, we can use pull command:
  **docker pull 'container-name'**: This command pulls the container from docker hub and saves it locally.

---
> ## ps is the older way. Now a days we use ls (docker container ls, docker image ls, docker volume ls etc.)

1. **docker system prune -a** : To remove all stopped containers, all networks not used by at least one container, all
   unused images and all build cache from system.
2. **docker container prune**: It will remove all the stopped containers.
3. **docker image prune -a**: It will remove all the unused images.
4. **docker image ls** : To list all images.
5. **docker container ls** : To list all running containers
6. **docker container ls -a** : To list all containers
7. **docker image rm 'image-id1' 'image-id2** : To remove image/images
8. **docker container rm 'container-id1/container-name1' 'container-id2/container-name2'**: To remove
   container/containers
9. **docker run --rm 'image_name'** : This command runs a container and removes it after container completes it's
   execution'
10. **docker container ps -a** : To list all containers
11. **docker container ps** : To list all running containers
12. **docker volume ls** : To list all volumes
13. **docker container stop 'container-id'**: To stop a docker container

---

## Docker exec ##

When running containers, you often want to run commands in order to have access to a Shell instance or to start a CLI to
manage your servers. Luckily we have a command that we can use in order to execute commands on running containers:
**docker exec**.

- Best way to do it is, start a bash shell and use all CLI scripts to play with docker container.

```
docker exec -it 'container id' sh // curious what is -it doing here, Learn file descriptors(stdin stout sterr) in linux.
```
