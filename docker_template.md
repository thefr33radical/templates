#### List Docker containers (running, all, all in quiet mode)
```sh
docker container ls
docker container ls --all
docker container ls -aq
```

#### Docker stop
```sh
sudo docker container stop [ImageId]
```

#### Execute Docker image
```sh
docker run "image_name
```

#### Build Docker image
```
docker build -t "image_name" .
```

#### Remove images
```
remove images
docker system prune -a
```

#### Execute docker shell
```
sudo docker start [ImageID]
sudo docker exec -ti [ImageID] /bin/bash
sudo docker cp path_file_name [ImageID]:/path_file_name
```

#### List Docker CLI commands
```
docker
docker container --help
```

#### Display Docker version and info
```
docker --version
docker version
docker info
```
docker image ls
## List Docker CLI commands
docker
docker container --help

## Display Docker version and info
docker --version
docker version
docker info

## Execute Docker image
docker run hello-world

## List Docker images
docker image ls

## List Docker containers (running, all, all in quiet mode)
docker container ls
docker container ls --all
docker container ls -aq

docker build -t "image_name" .

remove images
docker system prune -a

#execute docker shell
sudo docker start [ImageID]
sudo docker exec -ti [ImageID] /bin/bash
sudo docker cp path_file_name [ImageID]:/path_file_name

#Docker stop
sudo docker container stop [ImageId]

sudo docker rm -f $(docker ps -a -q)

# Delete every Docker image
sudo docker rmi -f $(docker images -q)

### References
* https://codefresh.io/docker-tutorial/build-docker-image-dockerfiles/
* launch docker on EC2 - https://www.ybrikman.com/writing/2015/11/11/running-docker-aws-ground-up/
