#%%
import pandas as pd
import sklearn as sk
import numpy as np
import seaborn as sns

df = pd.read_csv("./data/heart.csv")
sns.pairplot(df)

# %%
df.corr()

# %%
df.columns
part_cols = []
tmp_cols = []

for idx, cols in enumerate(df.columns):
    tmp_cols.append(cols)
    if (idx % 4 == 0) and (idx != 0) :
        if "target" not in tmp_cols:
            tmp_cols.append("target")
        part_cols.append(tmp_cols)
        tmp_cols = []
if "target" not in tmp_cols:
    tmp_cols.append("target")
part_cols.append(tmp_cols)

# %%
df.columns
# %%
# paire1
sns.pairplot(df[part_cols[0]], hue="target")
# age 
# sex 男女差はありそう
# 
# %%
# paire2
sns.pairplot(df[part_cols[1]], hue="target")
# %%
# paire3
sns.pairplot(df[part_cols[2]], hue="target")

# %%
print(df[["sex", "target"]].value_counts())
print(df[["sex", "target"]].value_counts())
# 男性の方が心臓病になりやすい?

# %%
import matplotlib.pyplot as plt
import japanize_matplotlib

# wemale は 63?くらいが最頻値。比較的なだらか。
# male の場合、50-60に心臓病の山がある
# sex 0: 女性、1: 男性
plt.hist(df.loc[df["sex"]==1, ["age"]], color="r", alpha=0.3, label="male", bins=30)
plt.hist(df.loc[df["sex"]==0, ["age"]], color="b", alpha=0.3, label="wemale", bins=30)
plt.legend()
plt.xlabel("age[年齢]")
plt.ylabel("number")
plt.show()

# %%
# 男の心臓病の分布比較
# target 1: 心臓病, 0: そうじゃない
# sex 0: 女性, 1: 男性
plt.hist(df.loc[(df["sex"]==1) & (df["target"]==1), ["age"]], color="r", alpha=0.3, label="男病気", bins=30)
plt.hist(df.loc[(df["sex"]==1) & (df["target"]==0), ["age"]], color="b", alpha=0.3, label="男健康", bins=30)
plt.hist(df.loc[(df["sex"]==1), ["age"]], color="darkgray", alpha=0.3, label="男全体", bins=30)

plt.legend()
plt.xlabel("age[年齢]")
plt.ylabel("number")
plt.title("男性")
plt.show()

# %%
# 女性の心臓病、健康
# target 1: 心臓病, 0: そうじゃない
# sex 0: 女性, 1: 男性
plt.hist(df.loc[(df["sex"]==0) & (df["target"]==1), ["age"]], color="r", alpha=0.3, label="女病気", bins=30)
plt.hist(df.loc[(df["sex"]==0) & (df["target"]==0), ["age"]], color="b", alpha=0.3, label="女健康", bins=20)
plt.hist(df.loc[(df["sex"]==0), ["age"]], color="darkgray", alpha=0.3, label="女全体", bins=30)

plt.legend()
plt.xlabel("age[年齢]")
plt.ylabel("number")
plt.title("女性")
plt.show()


# %%
# sex 0: 女性, 1: 男性
# df.loc[(df["sex"]==0) & (df["target"]==0), ["sex"]].count()
df.loc[(df["sex"]==0) & (df["target"]==1), ["sex"]].count()


# %%
# sex 0: 女性, 1: 男性
df[["sex", "target"]].value_counts()
# 女性の方が心臓病の割合が高い
# 男性 300 / (300 + 413) = 0.42
# 女性 226 / (226 + 85) = 0.72


#%%
import japanize_matplotlib
# 女性は男性より健康状態が悪い?
# コレステロール
# sex 0: 女性, 1: 男性
plt.hist(df.loc[(df["sex"]==0), ["chol"]], color="r", alpha=0.3, label="女", bins=30)
plt.hist(df.loc[(df["sex"]==1), ["chol"]], color="b", alpha=0.3, label="男", bins=20)
plt.legend()
plt.xlabel("コレステロール（mg/dl）​")
plt.ylabel("数​")
plt.title("コレステロール男女差")
plt.show()

# 女性の方が分布が広い


# %%
import japanize_matplotlib
plt.hist(df.loc[(df["sex"]==0) & (df["target"]==1), ["chol"]], color="r", alpha=0.3, label="女病気", bins=30)
plt.hist(df.loc[(df["sex"]==0) & (df["target"]==0), ["chol"]], color="b", alpha=0.3, label="女健康", bins=20)
plt.legend()
plt.xlabel("コレステロール（mg/dl）​")
plt.ylabel("数​")
plt.title("コレステロール男女差")
plt.show()

# 女性のtarget=1, 0 で差があるかどうか
# 200-300mg/dl で病気が多い。 健常者も200-300mg/dl が多い。
# 健康な人の分布が長い

# %%

#%%
plt.hist(df.loc[(df["sex"]==0) & (30 <= df["age"]) & (df["age"] < 40) & (df["target"]==1), ["chol"]], color="r", alpha=0.3, label="女病気30代", bins=5)
# plt.hist(df.loc[(df["sex"]==0) & (40 <= df["age"]) & (df["age"] < 50) & (df["target"]==1), ["chol"]], color="b", alpha=0.3, label="女病気40代", bins=20)
# plt.hist(df.loc[(df["sex"]==0) & (50 <= df["age"]) & (df["age"] < 60) & (df["target"]==1), ["chol"]], color="c", alpha=0.3, label="女病気50代", bins=20)
plt.hist(df.loc[(df["sex"]==0) & (60 <= df["age"]) & (df["target"]==1), ["chol"]], color="m", alpha=0.3, label="女病気60以上", bins=30)
plt.legend()
plt.xlabel("コレステロール（mg/dl）​")
plt.ylabel("数​")
plt.title("コレステロール男女差")
plt.show()

# %%
# 各年代の数を数える(女性病気)
print(
    "30代", df.loc[(df["sex"]==0) & (30 <= df["age"]) & (df["age"] < 40) & (df["target"]==1), ["chol"]].count()[0],
    "40代",
    df.loc[(df["sex"]==0) & (40 <= df["age"]) & (df["age"] < 50) & (df["target"]==1), ["chol"]].count()[0],
    "50代",
    df.loc[(df["sex"]==0) & (50 <= df["age"])  & (df["age"] < 60)& (df["target"]==1), ["chol"]].count()[0],
    "60以上",
    df.loc[(df["sex"]==0) & (60 <= df["age"]) & (df["target"]==1), ["chol"]].count()[0]
)
#%%
# 各年代の数を数える(女性健康)
print(
    "30代", df.loc[(df["sex"]==0) & (30 <= df["age"]) & (df["age"] < 40) & (df["target"]==0), ["chol"]].count()[0],
    "40代",
    df.loc[(df["sex"]==0) & (40 <= df["age"]) & (df["age"] < 50) & (df["target"]==0), ["chol"]].count()[0],
    "50代",
    df.loc[(df["sex"]==0) & (50 <= df["age"]) & (df["age"] < 60) & (df["target"]==0), ["chol"]].count()[0],
    "60以上",
    df.loc[(df["sex"]==0) & (60 <= df["age"]) & (df["target"]==1), ["chol"]].count()[0]
)

##############################

#%%
# %%
# 各年代の数を数える(男性病気)
print(
    "30代", df.loc[(df["sex"]==1) & (30 <= df["age"]) & (df["age"] < 40) & (df["target"]==1), ["chol"]].count()[0],
    "40代",
    df.loc[(df["sex"]==1) & (40 <= df["age"]) & (df["age"] < 50) & (df["target"]==1), ["chol"]].count()[0],
    "50代",
    df.loc[(df["sex"]==1) & (50 <= df["age"])  & (df["age"] < 60)& (df["target"]==1), ["chol"]].count()[0],
    "60以上",
    df.loc[(df["sex"]==1) & (60 <= df["age"]) & (df["target"]==1), ["chol"]].count()[0]
)
#%%
# 各年代の数を数える(男性健康)
print(
    "30代", df.loc[(df["sex"]==1) & (30 <= df["age"]) & (df["age"] < 40) & (df["target"]==0), ["chol"]].count()[0],
    "40代",
    df.loc[(df["sex"]==1) & (40 <= df["age"]) & (df["age"] < 50) & (df["target"]==0), ["chol"]].count()[0],
    "50代",
    df.loc[(df["sex"]==1) & (50 <= df["age"]) & (df["age"] < 60) & (df["target"]==0), ["chol"]].count()[0],
    "60以上",
    df.loc[(df["sex"]==1) & (60 <= df["age"]) & (df["target"]==1), ["chol"]].count()[0]
)


# %%
# 女性の方が心臓病が高いと言えるのか？
# これを説明するには、男性より女性の方が健康が悪い人が多い？
# 重要な指標は症状(胸の痛み)、健康状態(コレステロール、血圧)

# 下記の記事によると
# 「発症したら、男性は胸の真ん中に激しく圧迫感がある典型的な症状が多い。一方、女性は非典型的にいろんな症状で発症する。すごく胸が苦しいのに加え、胸の違和感程度の場合や、肩の痛みなどさまざま」
# 症状として出るのは少ないという認識。
# https://www.tokyo-np.co.jp/article/389047



################
# 
# - 女性は男性より不健康?コレステロールの値が高い?
# - 他の要因?何かある?





############
# エストロゲン
# エストロゲン(女性ホルモン)は血管の保護などをする作用がある。エストロゲンが減ると心臓病になりやすい
# 45-50歳より若い時は、女性の方がエストロゲンが多く分泌される。45-50歳より年齢が高いと女性は心臓病になりやすい
# 男性ホルモンにも血管を保護する機能はあるが、女性ホルモンほど強い機能ではない。また、男性の場合は穏やかに減少する。
# https://www.nikkei.com/nstyle-article/DGXZQOFK071MG0X00C22A6000000/

# 40歳より前は女性ホルモン多い、40-50で女性ホルモン低下、50以降はほぼ分泌されない。
# 一つの指標になるのでは?
# https://www.fsight.jp/articles/-/48939



# 本データでは「男性より女性の方が心臓病の割合が高い」と言える。
# そもそも心臓病とは何...?
# 「女性の死亡率は男性のほぼ2倍」という記載がある。
# https://mainichi.jp/articles/20230925/k00/00m/040/205000c
# 一方、「生命予後」では、死亡率に大きな差がないという記事もある
# target はデータの取り方によって
# https://enoki-iin.com/contents/news/20240415_01.html


# ここまでで言えること
# 女性は心臓病の症状が出づらい
# 若い時は、男性の方が心臓病になりやすく、老いると女性の方が心臓病になりやすい
# このデータは40歳以上の女性のデータを集めている。心臓病の割合が必然的に高くなる。


