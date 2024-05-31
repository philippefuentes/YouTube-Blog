#!/bin/sh

# pour debug de l'immage docker pour lambda
# 1 => docker run -d  --name yt-search-image-deploy yt-search-image-deploy
# 2 => docker exec -it yt-search-image-deploy /bin/bash
docker build -f Dockerfile-deploy -t yt-search-image-deploy .

