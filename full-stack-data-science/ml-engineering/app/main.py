# import numpy as np
# import polars as pl
from fastapi import FastAPI
from mangum import Mangum

# ref: https://stackoverflow.com/questions/76851281/setting-up-a-sentencetransformer-with-aws-lambda
from sentence_transformers import SentenceTransformer

# from sklearn.metrics import DistanceMetric
# from app.functions import returnSearchResultIndexes

# # define model info
# model_name = 'all-MiniLM-L6-v2'
# model_path = "app/data/" + model_name
#
# # load model
# model = SentenceTransformer(model_path)
#
# # load video index
# df = pl.scan_parquet('app/data/video-index.parquet')
#
# # create distance metric object
# dist_name = 'manhattan'
# dist = DistanceMetric.get_metric(dist_name)


# create FastAPI object
app = FastAPI()

# API operations
@app.get("/")
def health_check():
    return {'health_check': 'OK'}

@app.get("/info")
def info():
    return {'name': 'yt-search', 'description': "Search API for Shaw Talebi's YouTube videos."}

# @app.get("/search")
# def search(query: str):
#     idx_result = returnSearchResultIndexes(query, df, model, dist)
#     return df.select(['title', 'video_id']).collect()[idx_result].to_dict(as_series=False)

handler = Mangum(app)