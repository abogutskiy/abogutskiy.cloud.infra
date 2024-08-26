#!/bin/bash

SCRIPT=$(readlink -f "$0")
DIR=$(dirname "$SCRIPT")

sudo $DIR/deploy_configs.py $(dirname "$DIR")/configs/deploy_config.json

sudo systemctl daemon-reload
sudo systemctl enable  abogutskiy.cloud.service
sudo systemctl start abogutskiy.cloud.service
