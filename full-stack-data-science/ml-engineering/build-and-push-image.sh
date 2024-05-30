#!/bin/sh

docker build -f Dockerfile-deploy -t yt-search-image .
docker tag yt-search-image:latest 294263178210.dkr.ecr.us-east-1.amazonaws.com/yt-search-demo:latest
docker push 294263178210.dkr.ecr.us-east-1.amazonaws.com/yt-search-demo:latest

