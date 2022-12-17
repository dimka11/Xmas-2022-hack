import pandas as pd

import pandas as pd
from datetime import datetime, timedelta
import numpy as np
import os
import json
import matplotlib.pyplot as plt
import seaborn as sns


def diff_data_range(start_date='2022-11-21', end_date='2022-12-12', field='close', return_pandas=True, save_json=True,
                    json_path_dir='./data', shares=pd.read_csv('./data/shares_lm.csv')):
    shares_start = shares[
        (shares['datetime'] >= f'{start_date} 10:00:00') & (shares['datetime'] <= f'{start_date} 13:00:00')]
    shares_end = shares[(shares['datetime'] >= f'{end_date} 10:00:00') & (shares['datetime'] <= f'{end_date} 13:00:00')]

    codes_start = shares_start.groupby(['code']).first().index
    codes_end = shares_end.groupby(['code']).first().index

    close_diff = shares_end.groupby(['code']).first().reindex(codes_start).dropna()[field] - \
                 shares_start.groupby(['code']).first().reindex(codes_end).dropna()[field]

    res = close_diff.sort_values(ascending=False)

    if save_json:
        path = f'{json_path_dir}/{start_date}_{end_date}_diff.json'

        with open(path, 'w+') as f:
            f.write(res.to_json())

    if return_pandas:
        return res


def get_end_date():
    today = datetime.today()
    end_date = today - timedelta(days=3)
    return end_date.strftime('%Y-%m-%d')


def get_start_date(minus_days=7):  # 7 14 21 27
    today = datetime.today()
    end_date = today - timedelta(days=3)
    start_date = end_date - timedelta(days=minus_days)
    return start_date.strftime('%Y-%m-%d')


def get_last_week_date():
    shares_lm = pd.read_csv('./data/shares_lm.csv')

    top_5_last_week = diff_data_range(start_date='2022-12-05', end_date='2022-12-12').head(5)
    low_5_last_week = diff_data_range(start_date='2022-12-05', end_date='2022-12-12').tail(5)

    last_week_dict = {}

    for i, items in pd.concat([top_5_last_week, low_5_last_week]).iteritems():
        last_week_dict.update({i: [int(shares_lm[shares_lm['code'] == i].tail(1)['close'].values[0]), int(items)]})
    return last_week_dict


def filter_data(data, num=-100):
    shares_lm = pd.read_csv('./data/shares_lm.csv')

    shares_lm['datetime'] = pd.to_datetime(shares_lm['datetime'])
    grb_res = shares_lm.groupby(['code', shares_lm['datetime'].dt.date]).mean().diff()[
        shares_lm.groupby(['code', shares_lm['datetime'].dt.date]).mean().diff() < 0].groupby(['code']).mean()['vol']
    for i, item in data.iteritems():
        if grb_res[i] < num:
            print(grb_res[i])
            data.drop(i, inplace=True)

    return data
