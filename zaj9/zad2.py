import pandas as pd

iris = pd.read_csv("iris.csv")

#Create numeric classes for species (0,1,2)
iris.loc[iris['species']=='virginica','species']=0
iris.loc[iris['species']=='versicolor','species']=1
iris.loc[iris['species']=='setosa','species'] = 2
iris = iris[iris['species']!=2]

#Create Input and Output columns
X = iris[['petal_length', 'petal_width']].values.T
Y = iris[['species']].values.T
Y = Y.astype('uint8')
