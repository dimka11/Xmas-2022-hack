import pandas as pd

import pandas as pd
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
