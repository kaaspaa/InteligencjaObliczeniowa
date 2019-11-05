import pandas as pd
import numpy as np

df = pd.read_csv("iris_with_errors.csv")
count1 = 0
bad_val = ['n/a', 'na', '-', '--', '']
varieties = ["Virginica", "Setosa", "Versicolor"]

#a)
print("a) Policz ile jest w bazie brakujących lub nieuzupełnionych danych. Wyświetl statystyki bazy danych z  błędami.\n")
if df[df["sepal.length"].isin(bad_val)].values.any():
    print(df[df["sepal.length"].isin(bad_val)])
if df[df["sepal.width"].isin(bad_val)].values.any():
    print(df[df["sepal.width"].isin(bad_val)])
if df[df["petal.length"].isin(bad_val)].values.any():
    print(df[df["petal.length"].isin(bad_val)])
if df[df["petal.width"].isin(bad_val)].values.any():
    print(df[df["petal.width"].isin(bad_val)])
if df[df["variety"].isin(bad_val)].values.any():
    print(df[df["variety"].isin(bad_val)])
if df[~df["variety"].isin(varieties)].values.any():
    print(df[~df["variety"].isin(varieties)])

#b)
print("\nb) Sprawdź czy wszystkie dane numeryczne są z zakresu (0; 15). Dane spoza zakresu muszą być poprawione. Możesz tutaj użyć metody: za błędne dane podstaw średnią (lub medianę) z danej kolumny.\n")
df2 = pd.read_csv("iris_with_errors.csv", na_values=bad_val)
for i in range(df.shape[0]):
    #sepal.length
    if df.loc[i]["sepal.length"] in bad_val:
        df.set_value(i, "sepal.length", df2.loc[:, "sepal.length"].median())
    elif float(df.loc[i]["sepal.length"]) > 15 or float(df.loc[i]["sepal.length"]) < 0 :
        df.set_value(i, "sepal.length", df2.loc[:, "sepal.length"].median())
    #sepal.width
    if df.loc[i]["sepal.width"] in bad_val:
        df.set_value(i, "sepal.width", df2.loc[:, "sepal.width"].median())
    elif float(df.loc[i]["sepal.width"]) > 15 or float(df.loc[i]["sepal.width"]) < 0 :
        df.set_value(i, "sepal.width", df2.loc[:, "sepal.width"].median())
    #petal.length
    if df.loc[i]["petal.length"] in bad_val:
        df.set_value(i, "petal.length", df2.loc[:, "petal.length"].median())
    elif float(df.loc[i]["petal.length"]) > 15 or float(df.loc[i]["petal.length"]) < 0 :
        df.set_value(i, "petal.length", df2.loc[:, "petal.length"].median())
    #petal.width
    if df.loc[i]["petal.width"] in bad_val:
        df.set_value(i, "petal.width", df2.loc[:, "petal.width"].median())
    elif float(df.loc[i]["petal.width"]) > 15 or float(df.loc[i]["petal.width"]) < 0 :
        df.set_value(i, "petal.width", df2.loc[:, "petal.width"].median())

#sprawdzenie czy sa jeszcze jakies zle wartosci:
if df[df["sepal.length"].isin(bad_val)].values.any():
    print(df[df["sepal.length"].isin(bad_val)])
if df[df["sepal.width"].isin(bad_val)].values.any():
    print(df[df["sepal.width"].isin(bad_val)])
if df[df["petal.length"].isin(bad_val)].values.any():
    print(df[df["petal.length"].isin(bad_val)])
if df[df["petal.width"].isin(bad_val)].values.any():
    print(df[df["petal.width"].isin(bad_val)])

#c)
print("c)Sprawdź czy wszystkie gatunki są napisami: „Setosa”, „Versicolor” lub „Virginica”. Jeśli nie, należy je poprawić.")
for i in range(df.shape[0]):
    if df.loc[i]["variety"] not in varieties:
        print("Przed:")
        print(df.loc[i]["variety"])
        if df.loc[i]["variety"] == "Versicolour":
            df.set_value(i, "variety", "Virginica")
        variet = list(df.loc[i]["variety"])
        first_letter = variet[0]
        variet[0] = first_letter.upper()
        variet = ''.join(variet)
        df.set_value(i, "variety", variet)
        print("Po:")
        print(df.loc[i]["variety"])
