import pandas as pd
from sklearn import datasets

def myPredictRow(sl, sw, pl, pw):
    if pw < 0.5 :
        return "Iris-setosa"
    elif pl < 5:
        return "Iris-versicolor"
    else:
        return "Iris-virginica"

df = pd.read_csv("iris.csv")
eval = 0
for i in range(df.shape[0]):
    if df.loc[i]["class"] == myPredictRow(df.loc[i]["sepallength"], df.loc[i]["sepalwidth"], df.loc[i]["petallength"], df.loc[i]["petalwidth"]):
        eval += 1
        print(df.loc[i]["class"])
print("eval = " + str(eval) + "/" + str(150))
#iris = datasets.load_iris()
#digits = datasets.load_digits()
#print(digits.data)