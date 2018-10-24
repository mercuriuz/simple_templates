#!/bin/bash
REPO=zhipeng
CONTAINER=simple-python3
TAG=$(date '+%Y%m%d')-$(git rev-parse --short HEAD)

DOCKER_IMAGE=$REPO/$CONTAINER:$TAG

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BUILDROOT=$DIR/..

DOCKERFILE=$DIR/Dockerfile

# Build docker
cmd="docker build -t $DOCKER_IMAGE -f $DOCKERFILE $BUILDROOT"
echo $cmd
eval $cmd
