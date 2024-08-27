#!/usr/bin/env bash

SCRIPT=$(readlink -f "$0")
DIR=$(dirname "$SCRIPT")

sudo $DIR/deploy_configs.py --config=$(dirname "$DIR")/configs/production/deploy_config.json

# for wireguard ipv6 support
sudo modprobe ip6_tables

sudo systemctl daemon-reload
SERVICE=abogutskiy.cloud.service
sudo systemctl enable $SERVICE

if systemctl is-active --quiet $SERVICE; then
    echo "$SERVICE is running, restarting..."
    sudo systemctl restart $SERVICE
else
    echo "$SERVICE is not running, starting..."
    sudo systemctl start $SERVICE
fi

