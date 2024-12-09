import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# 加载数据
def load_data(C:\\Users\\UNIVERGY_konta\\Desktop\\demand-forecast\\sqldata.csv):
    df = pd.read_csv(file_path, index_col='Date', parse_dates=True)
    return df
