#!/bin/bash

container="flaskAPI"
ip="172.19.0.6"

docker rm -f $container
docker run --name $container --hostname $container --network=brlgr --ip=$ip -v /data/rsyncAPI/app:/app:rw -v /home/lgr/CDN:/app/cdn:ro --restart always -d mini-api