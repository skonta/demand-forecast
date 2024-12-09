# 将 year, month, day 组合成一个日期列
data['Date'] = pd.to_datetime(data[['year', 'month', 'day']])

# 设置 Date 列为索引，按照时间顺序排序
data.set_index('Date', inplace=True)
data.sort_index(inplace=True)

# 选择需要的特征列 (假设 seg1 到 seg48 是你感兴趣的特征)
features = [col for col in data.columns if col.startswith('seg')]

# 提取这些特征用于后续处理
df = data[features]

# 归一化处理
scaled_data, scaler = normalize_data(df)

# 创建时间序列数据集
X, y = create_dataset(scaled_data, time_step=60)

print(f"X shape: {X.shape}")
print(f"y shape: {y.shape}")
