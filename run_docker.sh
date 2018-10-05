#!/bin/bash

container="flaskAPI"

docker rm -f $container
docker run --name $container --hostname $container -p 80:80 --restart always -d mini-api
