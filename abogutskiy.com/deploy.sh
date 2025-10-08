#!/usr/bin/env bash

SCRIPT=$(readlink -f "$0")
DIR=$(dirname "$SCRIPT")

sudo mkdir -p /etc/docker/abogutskiy.com/
sudo cp compose.yaml /etc/docker/abogutskiy.com/
sudo chown -R www-data:www-data /etc/docker/abogutskiy.com/
sudo cp abogutskiy.com.service /etc/systemd/system/

sudo systemctl daemon-reload
SERVICE=abogutskiy.com.service
sudo systemctl enable $SERVICE

if systemctl is-active --quiet $SERVICE; then
    echo "$SERVICE is running, restarting..."
    sudo systemctl restart $SERVICE
else
    echo "$SERVICE is not running, starting..."
    sudo systemctl start $SERVICE
fi

