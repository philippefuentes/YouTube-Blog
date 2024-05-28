# AWS deployment using API Gateway + Lambda

- use of `Mangum` to allow FastAPI to handle Lambda events


## build image

```
docker build -t yt-search-image .
docker build -f Dockerfile-deploy -t yt-search-image .

```
## run image (test)

```
docker run -d --name yt-search-container -p 8082:80 yt-search-image

# debug the container
docker exec -it yt-search-container /bin/bash
```

## push image to ECR

```
# login to ECR
./login-ecr-eussam.sh

# tag
docker tag yt-search-image:latest 294263178210.dkr.ecr.us-east-1.amazonaws.com/yt-search-demo:latest

# push
docker push 294263178210.dkr.ecr.us-east-1.amazonaws.com/yt-search-demo:latest
```
## troubleshooting

- lambda env

`Error in cpuinfo: failed to parse the list of present processors in /sys/devices/system/cpu/present`

solution: install CPU-only version of PyTorch as Lambda does not use GPU:

add in requirements.txt:

```
--extra-index-url https://download.pytorch.org/whl/cpu
torch
```




## tips

- check dependencies of the project

```
pip show sentence-transformers
pip list
pip freeze
```
