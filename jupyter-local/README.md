# Manual installation of Jupyter Notebook (in local machine or a server).

## Objective and introduction

This tutorial will help as a guide to set up Jupyter Notebook in a local or remote server Ubuntu 18.04 and, also, to describe how to connect to that Notebook and use it.

***What is Jupyter Notebooks***

Jupyter Notebook (or simply Notebooks) is a set of documents that are produced to be handle by the Jupyter Notebook application.

A notebook is a sum of pieces of code, markdown text and the outputs. As a single document, it is helping to share with others.

***Pre-requisites***

To use this guide, you must have:
- An Ubuntu 18.04 server
- A basic firewall
- One user (no root) with admin privileges be able to execute sudo commands. 

## Step 1: Python configuration

To start, all Python dependencies will be installed. When Ubuntu 18.04 is installed, automatically a Python 3.6 is also installed. So, the Python package manager (*pip*) will be used to install any additional packages later.

First, update the package administration manager *apt* :

    sudo apt update

Then, install *pip* and the python development:

    sudo apt install python3-pip python3-dev

Now, we can progres to Step 2 to install and configure the virtual environment to install Jupyter. (optional)

## Step 2 (optional): Set up a Python virtual environment for Jupyter

When python3, python3-dev and pip are installed, the virtual environment can be set up.

To do this, first access to *virtualenv* command is required. 

It is possible to install with *pip*. So, first update pip and install:

    sudo -H pip3 install --upgrade pip
    sudo -H pip3 install virtualenv

Note: The -H modifier will guarantee that the security policy will define a environment variable "home" with the target user directory as the initial directory for the environment.

When *virtualenv* is installed, then it is possible to start to create the environment. To do this, first a directory must be created. This directory will contain all the files of our project. It is required to be in that directory prior to open the project. The name of that directory must have a significative name for the work you are doing:
In our case, as it is related to the Jupyter installation, it will named "jupyter-dir".

    mkdir ~/jupyter-dir
    cd ~/jupyter-dir

From inside the project directory, the environment will be started. The name will be "jupyter-env" as related to this Jupyter guideline.

    virtualenv jupyter-env

With this command, a jupyter-env directory will be created under jupyter-dir directory. In that directory, a local python and local pip will be installed autormatically. Those commands will be used to configure a specific environment for the Jupyter installation.

To activate that virtual environment:

    source my_project_env/bin/activate (en nuestro caso, jupyter-env/bin/activate )

Now, the prompt line will show something similar to *(jupyter-env) user@host:~/jupyter-dir$* where user will be your username and host the corresponding name of your host machine.

Now, everything is ready to install Jupyter in this virtual environment.

## Step 3: Jupyter installation and configuration

When the virtual environment is activated, a Jupyter installation is possible with the local pip.

Note: Inside virtual environment, *pip* could be used instead *pip3*.

    pip install jupyter

So, Jupyter has been installed succesfully. But some configuration must be adapted.

To do the configuration, edit with nano (or any other editing tool):

    nano ~/.jupyter/jupyter_notebook_config.py

In the configuration file, the following options will be activated and set up:

    c.NotebookApp.allow_password_change = True
    c.NotebookApp.allow_root = True
    c.NotebookApp.ip = "localhost " (or set the remote host IP)
    c.NotebookApp.notebook_dir = 'jupyter-dir/runbooks/'
    c.NotebookApp.open_browser = False

Please, notice that a default directory for runbooks is set.

Now the Notebook server can be started.

## Step 4: Run Jupyter Notebook in a local machine

Simply write the following line to run Jupyter notebook:

    jupyter notebook

To acess the notebooks, a URL will be shown in the screen with the http://host:port/?token=xxxxxxxxxx like the below example: 

    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token: http://localhost:8888/?token=1fefa6ab49a498a3f37c959404f7baf16b9a2eda3eaa6d72

- If you are running Jupyter Notebook in a local computer, then simply type the URL in a browser.
- If you are running in a server, then connect with a SSH tunneling service as described in *Step 5 and 6*

To stop the notebook, just press *CTRL+C*

## Step 5: Connect with a SSH tunneling from a Linux system

To create the tunnel to the remote system, type the next command to map ports and stablish the connection (assuming the port 8888 is used in the default installation, if not, set your appropiate port number):

    ssh -L 8888:localhost:8888 server_username@server_ip

If the command is executed sucessfully, and the connection is well stablish, then type

    jupyter notebook

and then you can access the books in the URL.

## Step 6: Using Jupyter Notebook

Now, you are ready to use Jupyter Notebook in a browser. Enjoy it!!
