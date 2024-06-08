#!/bin/sh

# docker build -f Dockerfile-deploy -t yt-search-image-deploy .
# docker tag yt-search-image-deploy:latest 294263178210.dkr.ecr.us-east-1.amazonaws.com/yt-search-demo:latest
# docker push 294263178210.dkr.ecr.us-east-1.amazonaws.com/yt-search-demo:latest

# run the container locally
# docker run --name yt-search-container -p 8082:80 --entrypoint "" yt-search-image-deploy fastapi run app/main.py --port 80

CONTAINER_NAME="yt-search-container"
IMAGE_NAME="yt-search-image-deploy"
PORT_MAPPING="8082:80"
ENTRYPOINT=""
COMMAND="fastapi run app/main.py --port 80"

# Check if the container is already running
# Check if the container exists (running or stopped)
if [ "$(docker ps -a -q -f name=$CONTAINER_NAME)" ]; then
    # Stop and remove the container if it exists
    echo "Stopping and removing the existing container..."
    docker rm -f $CONTAINER_NAME
fi

# Run the new container
echo "Running the new container..."
docker run --name $CONTAINER_NAME -p $PORT_MAPPING --entrypoint "$ENTRYPOINT" $IMAGE_NAME $COMMAND
