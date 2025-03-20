import pandas as pd

# 读取数据
df = pd.read_csv('data/b202203.csv')

# 按 90% 训练集和 10% 测试集划分数据
train = df.sample(frac=0.9, random_state=42)
test = df.drop(train.index)

# 保存划分后的数据
train.to_csv('data/train1.csv', index=False)
test.to_csv('data/test1.csv', index=False)
