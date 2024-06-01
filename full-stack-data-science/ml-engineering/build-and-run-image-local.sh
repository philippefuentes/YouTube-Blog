#!/bin/sh

# build
docker build -f Dockerfile -t yt-search-image .
# run the container
docker run -d --name yt-search-container -p 8082:80 yt-search-image
