#!/bin/sh

docker build -f Dockerfile-deploy -t yt-search-image-deploy .
docker tag yt-search-image-deploy:latest 294263178210.dkr.ecr.us-east-1.amazonaws.com/yt-search-demo:latest
docker push 294263178210.dkr.ecr.us-east-1.amazonaws.com/yt-search-demo:latest

# run the container locally
docker run --name yt-search-container -p 8082:80 --entrypoint "" yt-search-image-deploy fastapi run app/main.py --port 80
