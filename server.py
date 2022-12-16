import json
import os
import pathlib

from fastapi import FastAPI, Form, Request, Body
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from typing import Union, List

import uvicorn
import yaml

app = FastAPI(debug=True)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Keyword(BaseModel):
    keyword: str


# @app.post("/fit")
# def fit_model(keyword: Keyword):
#     start_training(keyword.keyword)
#     config = get_status_config()

#     return {"status": config['model_status'], "error": ""}


@app

app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)