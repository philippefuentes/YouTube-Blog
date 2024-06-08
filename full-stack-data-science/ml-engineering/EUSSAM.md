# notes sur le déploiement du container api sur lambda + gateway API

## utilisation de serverless framework pour déployer lambda + api gateway

### lambda container

- base image

```
FROM public.ecr.aws/lambda/python:3.10
```

- FastAPI + Lmabda handler

Mangum permet de garder la définition d'un app FastApi en étant compatible Lamnda handler

```
handler = Mangum(app)
```

- prod and dev config

On peut utiliser le container lambda de prod pour le lancer en local en écrasant le entrypoint pour lancer le server FastAPI:

```
docker run --name yt-search-container -p 8082:80 --entrypoint "" yt-search-image-deploy fastapi run app/main.py --port 80
```


### lamnbda context troubleshooting

- set environment variables to avoid CPU info parsing issues

```
# set environment variables to avoid CPU info parsing issues
ENV MKL_THREADING_LAYER=GNU
ENV OMP_NUM_THREADS=1
ENV MKL_NUM_THREADS=1
```
