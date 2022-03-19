## Dockerizing your Application ##

- For this purpose we create a Dockerfile in the root of our application and write all the steps along with dependencies
  which are at least needed to run our application/software.
- Once you have created the Dockerfile, you can run the following command to build the image:

```
docker build -t 'put your image name(can be anything of your choice) .
```

- Now we need to run(create+start) the container using the image which we built:

```
docker container run -it -p YOUR_APP_PORT:NEW_MAPPED_PORT 'image-name'
```

--- 
[Docker Cheat Sheet](https://gist.github.com/bradtraversy/89fad226dc058a41b596d586022a9bd3)

## Networking in Docker ##

When a container is created, it has 3 internal private network options and some ip addresses which are assigned to it:

1. bridge: The bridge network is the default network.
2. none: The container will not have a network interface.
3. host: The container will have a network interface which is connected to the host.

```
docker container run redis ==> it gets the default network(bridge)
To run container on host network or none network, we need to specify the network option in the docker container run command:
docker container run redis --network=host
docker container run redis --network=none
```