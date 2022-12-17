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

from data_analysis import diff_data_range, get_start_date, get_end_date, get_last_week_date, filter_data

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
    risk: str  # 'Низкий' 'Средний' 'Высокий' 'Очень высокий'
    period: str  # 'Неделя' '2 недели' 'Месяц' '2 месяца'
    selectedShares: List[str]  # for filter of shares


def return_resp_shares(risk, period, shares):
    if period == 'Неделя':
        data = diff_data_range(start_date=get_start_date(7), end_date=get_end_date()).head(20)
    elif period == '2 недели':
        data = diff_data_range(start_date=get_start_date(14), end_date=get_end_date()).head(20)
    elif period == 'Месяц':
        data = diff_data_range(start_date=get_start_date(21), end_date=get_end_date()).head(20)
    else:
        data = diff_data_range(start_date=get_start_date(27), end_date=get_end_date()).head(20)

    if (risk == "Очень высокий") or (risk == "Bысокий"):
        dict_ = {}
        for i, item in data.iteritems():
            dict_.update({i: 150})
        return dict_

    if risk == "Низкий":
        data = filter_data(data, -100)

        dict_ = {}
        for i, item in data.iteritems():
            dict_.update({i: 150})
        return dict_

    if risk == "Средний":
        data = filter_data(data, -200)
        dict_ = {}
        for i, item in data.iteritems():
            dict_.update({i: 150})
        return dict_




def return_shares_adviced():
    return {"shares": list(diff_data_range(get_start_date(2), get_end_date())[:15].index)}


def return_shares_last():
    return get_last_week_date()


@app.get("/get_shares_last")
def get_shares_last():
    return return_shares_last()


@app.get("/get_advised")
def get_advised():
    return return_shares_adviced()


@app.post("/form_post")
def fit_model(form_post: FormPost):
    return return_resp_shares(form_post.risk, form_post.period, form_post.selectedShares)


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
