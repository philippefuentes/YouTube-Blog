# import numpy as np
# import polars as pl
import json
import os

from fastapi import FastAPI
from mangum import Mangum

# ref: https://stackoverflow.com/questions/76851281/setting-up-a-sentencetransformer-with-aws-lambda
from sentence_transformers import SentenceTransformer
from sklearn.metrics import DistanceMetric

from app.functions import returnSearchResultIndexes

#
# define model info
model_name = 'all-MiniLM-L6-v2'
# model_path = "app/data/" + model_name
# deploy
model_path = "/mnt/efs/" + model_name

# load model
model = SentenceTransformer(model_path)
#
# # load video index
# df = pl.scan_parquet('app/data/video-index.parquet')
#
# # create distance metric object
# dist_name = 'manhattan'
# dist = DistanceMetric.get_metric(dist_name)



def check_permissions(path):
    print(f"Checking permissions for path: {path}")
    permissions = {}
    for root, dirs, files in os.walk(path):
        for name in dirs + files:
            full_path = os.path.join(root, name)
            stat_info = os.stat(full_path)
            permissions[full_path] = {
                "mode": oct(stat_info.st_mode),
                "uid": stat_info.st_uid,
                "gid": stat_info.st_gid
            }
    return permissions




# create FastAPI object
app = FastAPI()

# API operations
@app.get("/")
def health_check():
    return {'health_check': 'OK'}

@app.get("/info")
def info():
    return {'name': 'yt-search', 'description': "Search API for Shaw Talebi's YouTube videos."}

@app.get("/perm")
def perm_check():
    # path = "/mnt/efs"

    path = "/mnt/efs"
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

    # try:
    #     st = os.stat(path)
    #     permissions = {
    #         "mode": oct(st.st_mode),
    #         "uid": st.st_uid,
    #         "gid": st.st_gid
    #     }
    #     return {"path": path, "permissions": permissions}
    # except Exception as e:
    #     return {"error": str(e)}


    # path = "/mnt/efs"
    # permissions = check_permissions(path)
    # return {
    #     "statusCode": 200,
    #     "body": json.dumps(permissions)
    # }

@app.get("/write-file")
def write_file():
    file_path = "/mnt/efs/hello.txt"
    with open(file_path, "w") as file:
        file.write("hello world")
    return {"message": "File written successfully", "file_path": file_path}

# @app.get("/search")
# def search(query: str):
#     idx_result = returnSearchResultIndexes(query, df, model, dist)
#     return df.select(['title', 'video_id']).collect()[idx_result].to_dict(as_series=False)

handler = Mangum(app)