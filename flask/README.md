# dockerflask

Just a tiny web server to play with. Primarily designed to build a docker image to launch a flask driven web server.

You can also launch the server by hand:
- sudo apt install python3-pip
- sudo pip3 install flask
- cd src
- python3 server.py
- Connect a browser to port 5000 for your "hello world" response

To build the docker image you need to:
- Install docker
- execute the build: docker build -t "my image name like myflask"

To run the docker image you'll need to:
- Have docker installed
- Have built the image. You can check it's on your system with 'docker images'
- You can run the image with this:
  - docker run --rm -p 5000:5000 "myflask"
    - --rm removes the image when you stop it
    - -p 5000:5000 maps port 5000 on your host OS to port 5000 of the container, making the web server 'visible' to the outside network.

To stop the image if it's detached from the console:
- use docker ps to find the NAME of the docker container
- docker stop "the running NAME"

Reminder: unless you've added your personal account to the docker Unix group, you'll have to run the docker commands with sudo.
