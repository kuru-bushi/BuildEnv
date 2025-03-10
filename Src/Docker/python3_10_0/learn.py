#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("/home/datasets/Housing.csv")
# Download below URL using browser UI.
# https://www.kaggle.com/datasets/yasserh/housing-prices-dataset?resource=download

# %%
x_name = "area"
y_name = "price"
plt.xlabel(x_name)
plt.ylabel(y_name)
plt.title("House_price")
plt.scatter(df[y_name], df[x_name])
plt.show()

# %%


