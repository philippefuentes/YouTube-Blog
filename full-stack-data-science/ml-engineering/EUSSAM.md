# notes sur le déploiement du container api sur lambda + gateway API

## utilisation de serverless framework pour déployer lamnda + api gateway

### lambda container

- base image

```
FROM public.ecr.aws/lambda/python:3.10
```

- FastAPI + lamnda handler

Mangum permet de de garder la définition d'un app FastApi en étant compatible Lamnda handler

```
handler = Mangum(app)
```

### lamnbda context troubleshooting

- set environment variables to avoid CPU info parsing issues

```
# set environment variables to avoid CPU info parsing issues
ENV MKL_THREADING_LAYER=GNU
ENV OMP_NUM_THREADS=1
ENV MKL_NUM_THREADS=1
```
