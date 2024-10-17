import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# 加载数据
def load_data(file_path):
    df = pd.read_csv(file_path, index_col='Date', parse_dates=True)
    return df

# 数据归一化
def normalize_data(df):
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(df[['Demand']].values)
    return scaled_data, scaler

# 创建时间序列数据
def create_dataset(data, time_step=60):
    X, y = [], []
    for i in range(len(data) - time_step):
        X.append(data[i:(i + time_step), 0])
        y.append(data[i + time_step, 0])
    return np.array(X), np.array(y)
