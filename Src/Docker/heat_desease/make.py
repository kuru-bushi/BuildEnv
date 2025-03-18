#%%
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


csv_path = "./data/heart.csv"
df = pd.read_csv(csv_path)


# まず、全体の20%をテストデータとし、残り80%を訓練＋検証データとする
train_val_data, test_data = train_test_split(df, test_size=0.2, random_state=42)

# 次に、訓練＋検証データの25%を検証データとし、残り75%を訓練データとする
train_data, val_data = train_test_split(train_val_data, test_size=0.2, random_state=42)


train_data.to_csv('./data/train_data.csv', index=False)
val_data.to_csv('./data/val_data.csv', index=False)
test_data.to_csv('./data/test_data.csv', index=False)


# %%
