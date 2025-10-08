#!/usr/bin/env bash

SCRIPT=$(readlink -f "$0")
DIR=$(dirname "$SCRIPT")

sudo mkdir -p /etc/docker/abogutskiy.com/
sudo cp compose.yaml /etc/docker/abogutskiy.com/
sudo touch /etc/docker/abogutskiy.com/.env
sudo chown -R www-data:www-data /etc/docker/abogutskiy.com/
sudo cp abogutskiy.com.service /etc/systemd/system/

NAME=abogutskiy.com
SERVICE=$NAME.service

IMAGE_ID=`docker image inspect -f '{{.Id}}' $NAME:latest`
docker build . -t $NAME:latest

sudo systemctl daemon-reload
sudo systemctl enable $SERVICE

if systemctl is-active --quiet $SERVICE; then
    echo "$SERVICE is running, restarting..."
    sudo systemctl restart $SERVICE
else
    echo "$SERVICE is not running, starting..."
    sudo systemctl start $SERVICE
fi


docker rm -f $(docker ps -a --filter "ancestor=$IMAGE_ID" --format "{{.ID}}") && docker image rm -f $IMAGE_ID


