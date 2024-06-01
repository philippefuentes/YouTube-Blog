import json
import os
import subprocess

import numpy as np
import polars as pl
import requests
from fastapi import FastAPI
from mangum import Mangum

# ref: https://stackoverflow.com/questions/76851281/setting-up-a-sentencetransformer-with-aws-lambda
from sentence_transformers import SentenceTransformer
from sklearn.metrics import DistanceMetric

from app.functions import returnSearchResultIndexes

# create FastAPI object
app = FastAPI()

# API operations
@app.get("/")
def health_check():
    # result = subprocess.run(['ls', '-lsa'], capture_output=True, text=True)
    # print(result.stdout)
    return {'health_check': 'OK'}

@app.get("/info")
def info():
    return {'name': 'yt-search', 'description': "Search API for Shaw Talebi's YouTube videos."}


@app.get("/publicip")
def get_public_ip():
    try:
        response = requests.get("http://ifconfig.me")
        public_ip = response.text
        return f"Public IP: {public_ip}"
    except requests.RequestException as e:
        return f"Error fetching public IP: {e}"


@app.get("/perm")
def perm_check():
    path = "/mnt/efs"
    # /mnt/efs/efs-hf-storage
    try:
        st = os.stat(path)
        permissions = {
            "mode": oct(st.st_mode),
            "uid": st.st_uid,
            "gid": st.st_gid
        }
        directory_contents = os.listdir(path)
        file_details = {}
        for item in directory_contents:
            item_path = os.path.join(path, item)
            item_stat = os.stat(item_path)
            file_details[item_path] = {
                "mode": oct(item_stat.st_mode),
                "uid": item_stat.st_uid,
                "gid": item_stat.st_gid
            }
        return {"path": path, "permissions": permissions, "contents": file_details}
    except Exception as e:
        return {"error": str(e)}


@app.get("/perm2/{dir:path}")
def perm_check2(dir: str):
    path = os.path.join("/mnt/efs", dir)
    try:
        st = os.stat(path)
        permissions = {
            "mode": oct(st.st_mode),
            "uid": st.st_uid,
            "gid": st.st_gid
        }
        directory_contents = os.listdir(path)
        file_details = {}
        for item in directory_contents:
            item_path = os.path.join(path, item)
            item_stat = os.stat(item_path)
            file_details[item_path] = {
                "mode": oct(item_stat.st_mode),
                "uid": item_stat.st_uid,
                "gid": item_stat.st_gid
            }
        return {"path": path, "permissions": permissions, "contents": file_details}
    except Exception as e:
        return {"error": str(e)}

@app.get("/write-file")
def write_file():
    file_path = "/mnt/efs/hello.txt"
    with open(file_path, "w") as file:
        file.write("hello world")
    return {"message": "File written successfully", "file_path": file_path}


@app.get("/download-model")
def download_model():
    # Try importing SentenceTransformer with error handling

    #
    # define model info
    # model_name = 'all-MiniLM-L6-v2'
    # model_path = "app/data/" + model_name
    # deploy
    # model_path = "/mnt/efs/hub/" + model_name

    # load model
    # model = SentenceTransformer(model_path)

    SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    return {"message": "Downloading model"}

@app.get("/search-local")
def search(query: str):
    # define model info
    model_name = 'all-MiniLM-L6-v2'
    model_path = "app/data/" + model_name
    # load model
    model = SentenceTransformer(model_path)

    # load video index
    df = pl.scan_parquet('app/data/video-index.parquet')

    # create distance metric object
    dist_name = 'manhattan'
    dist = DistanceMetric.get_metric(dist_name)

    idx_result = returnSearchResultIndexes(query, df, model, dist)
    return df.select(['title', 'video_id']).collect()[idx_result].to_dict(as_series=False)

@app.get("/search-hub")
def search_hub(query: str):

    try:
        # define model info
        model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    except Exception as e:
            return {"error": str(e)}
    # load video index
    df = pl.scan_parquet('app/data/video-index.parquet')

    # create distance metric object
    dist_name = 'manhattan'
    dist = DistanceMetric.get_metric(dist_name)

    idx_result = returnSearchResultIndexes(query, df, model, dist)
    return df.select(['title', 'video_id']).collect()[idx_result].to_dict(as_series=False)

handler = Mangum(app)
