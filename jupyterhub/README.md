## DevOpsLab
### Set JupyterHUB in one-single node installation

This repo is based upon the official JupyterHub Docker deploy

Project structure:
```
.
├── docker-compose.yaml
└── README.md
```

[_docker-compose.yaml_](docker-compose.yaml)
```
services:
  hub:
    image: jupyterhub
    ...
    ports:
      - 443:443
```
This compose file will create a PostGres DB (`hub-db`) and a JupyterHub (`jupyterhub`) instances..
IMPORTANT NOTICE: Port 443 on the host MUST NOT already in use.

## Deploy with docker-compose

```
$ docker-compose build
Building image "juypyterhub" ... done
...
$ docker-compose up -d
Creating network "juypyterhub_default" with the default driver
Creating volume "data" with default driver
...
Creating hub-db ... done
Creating jupyterhub ... done
Attaching to hub-db, jupyterhub
```

## Expected result

Listing containers must show two containers running and the port mapping as below:
```
$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
45e9b302d0f0        jupyterhub         "jupyterhub -f ..."      11 seconds ago       Up 10 seconds        0.0.0.0:443->443/tcp   jupyterhub
164f0553ed54        hub-db             "/run.sh"                10 seconds ago       Up 9 seconds         0.0.0.0:0->0/tcp       hub-db
```

Then you can launch each application using the below links in your local web browser:

* JupyterHub: [`http://localhost:443`](http://localhost:443)

Stop and remove the containers. Use `-v` to remove the volumes if looking to erase all data.
```
$ docker-compose down -v
```
