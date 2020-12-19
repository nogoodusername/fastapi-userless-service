#!/usr/bin/env bash

set -e # Script fails if docker build fails (has edge cases)

# Write build script as you like

docker build -t fastapi-userless-service -f ../app/DockerfileProd ../app