# flask-hw
Python homework - flask app with redis in docker container

# How to use
To run images without building, download archive with [images](https://drive.google.com/drive/folders/1RE5Ph7fBtX4NJbQxmgMj46skFyh6VXOQ?usp=sharing), docker-compose.yml file and run following commands:
```sh
docker load -i result.zip
docker-compose up
```
Alternativey, one could build images from source. For this, move to /hw directory and run:
```sh
docker-compose up
```
After that, move to http://localhost:5000.
