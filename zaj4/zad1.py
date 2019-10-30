import pandas as pd
import numpy as np

df = pd.read_csv("iris_with_errors.csv")
print(df.head())
count1 = 0
#print(df[df["variety"] == "Serota"])
filter = df['sepal.width'] == 3
df.set_index('variety', inplace=True)
df.where(filter,inplace=True)
print(df.all)
#for flower in df['variety']:
#    if flower.isnull():
#        count1 += 1
#        print(flower)
