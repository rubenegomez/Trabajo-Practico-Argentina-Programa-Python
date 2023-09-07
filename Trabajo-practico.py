import pandas as pd
import numpy as np
import datetime as dt
pd.DataFrame()

df = pd.read_csv("D:\RUBEN\Downloads\Spotify 2010 - 2021 Top 100.csv", sep=",")
df.info()
print(df)
indie = df[df["top genre"]== "indie rock"]["dur"].sum()
print(indie)