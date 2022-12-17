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

from data_analysis import diff_data_range

app = FastAPI(debug=True)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class FormPost(BaseModel):
    risk: str
    period: str
    selectedShares: List[str]


def return_resp_shares():
    return {"VSMO ": 150, "LNZL ": 150, "GMKN ": 150, "AAA ": 150}

def return_shares_adviced():
    return {"shares": ["VSMO", "LNZL", "GMKN", "AKRN", "VSYDP", "VJGZ", "CHMF", "SFIN", "AVAN", "SVAV",\
                       "GAZAP", "KAZTP", "SBERP", "LNZLP", "TATN"]}

def return_shares_last():
    return {"VSMO": [47520, -120], "LNZL": [14370, -960], "GMKN": [14282, 136], "AKRN": [17998, 48], "VSYDP": [4480, 40], \
            "PLZL": [7463, 232], "MGNT": [4382, -48], "KRKNP": [10160, 0], "KOGK": [33800, 400], "TRNFP": [84050, -1250]}


@app.get("/get_shares_last")
def get_shares_last():
    return return_shares_last()
@app.get("/get_advised")
def get_advised():
    return return_shares_adviced()

@app.post("/form_post")
def fit_model(form_post: FormPost):

    return return_resp_shares()


@app.get("/status")
def status():
    return {"status": 'fine'}


@app.get("/confirm")
def status():
    return {"status": 'confirmed'}


@app.post("/post_test")
async def post_test(request: Request):
    json = await request.json()
    return {'status': 'ok'}


app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)