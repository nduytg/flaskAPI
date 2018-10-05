#!/bin/bash

container="flaskAPI"

docker run --name $container --hostname $container -p 80:80 --restart always -d mini-api
