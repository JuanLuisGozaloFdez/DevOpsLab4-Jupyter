# DevOpsLab4-Jupyter

Lab for the DevOps Course, subject Monitoring. The lab will be used for installing Jupyter and a set of sample runbooks.

## Set Jupyter in one-single docker node installation with some runbooks for testing

The purpose of this lab is to show how to use Jupyter Notebooks to create and execute Operational RunBooks in DevOps.

Project structure:

```ascii
.
├── docker-compose.yml
├── jupyter
│   └── Dockerfile
├── data
└── runbooks
```

[_docker-compose.yml](docker-compose.yml)

```yaml
services:
  jupyter:
    build: 
      context: ./jupyter
    ports:
      - 8888:8888
      ...
```

This compose file will create a Jupyter (`jupyter`) docker instance.

*** IMPORTANT NOTICE ***: Port 8888 on the host MUST NOT already in use.

Runbooks will be saved in "runbooks" directory.

### Other Jupyter installations ***

In the repository, a Jupyterhub and a Direct Jupyter installation instructions are provided also, in case you prefer/need to follow those instead this docker instuction.

## Deploy with docker-compose

```bash
$ docker-compose build
Creating docker image "jupyter" ... done
...
$ docker-compose up -d
...
Creating volume "runbooks" with default driver
Creating jupyter ... done
$
```

## Expected result

Listing containers must show two containers running and the port mapping as below:

```bash
$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
45e9b302d0f0        jupyter            "jupyter -f ..."         11 seconds ago       Up 10 seconds       0.0.0.0:8888->8888/tcp   jupyter
$
```

## How to start using Jupyter

Execute the following command that get the token and URL link that is required to launch the envionment:

```bash
$ docker logs jupyter
... aplication can be found in the following ...
... http://127.0.0.1:8888/lab?token=xxxxxxxxxxxxxxxxxxxxxxxxxxxx ....
$
```

If you are accesing directly only with "http://localhost:8888" , then a LOGIN page will be shown asking for the TOKEN that you must obtain in the previous sentence.

After started, some example runbooks can be accesed from inside the Jupyter Lab desktop in the "runbook" folder of this repository (by default)

Stop and remove the containers. Use `-v` to remove the volumes if looking to erase all data.

```bash
$ docker-compose down -v
$
```

**Note**: Remember that when you open a noteboook, you must "Close and Halt" to stop the execution in the background of that notebook.

## How to test Jupyter notebook functionality

In the runbooks directory some examples notebooks have been deployed. All of them can be executed to see different jupyter notebook functionalities.

## How to test Jupyter Dashboard functionality

Jupyter Voilà is a Jupyter extension to provide Dashboard HTML capability. To test this functionality in this DevOpsLab then click in Voila icon inside any of the notebooks to see that the notebook is executed and an HTML with all the outputs is shown in a new window inside the lab interface.
