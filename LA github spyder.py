# -*- coding: utf-8 -*-

#Librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("LArealestate.csv")

#df.isna().sum()/df.shape[0]*100

df.dropna(inplace = True)

df["agency"] = df.date.apply(lambda x : x[10:])
df["date"] = df.date.apply(lambda x : x[:10])

df["street"] = df.address.apply(lambda x : " ".join(x.strip().split(" ")[1:]))
df["postal_code"] = df.address.apply(lambda x : (x.strip().split(" ")[0]))

df.drop("address", axis = 1, inplace = True)

df["year"] = df.date.apply(lambda x : x.split("/")[-1])
df["month"] = df.date.apply(lambda x : x.split("/")[1])
df["day"] = df.date.apply(lambda x : x.split("/")[0])

df.drop("date", axis = 1, inplace = True)
df.head()
