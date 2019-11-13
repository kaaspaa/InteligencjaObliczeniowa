import inline as inline
import matplotlib as matplotlib
import pandas as pd
import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.datasets import load_iris
from sklearn import tree
import graphviz

'exec(%matplotlib inline)'
df = pd.read_csv('iris.csv')
df['petalwidth'].plot.hist()
sns.pairplot(df, hue='class')
#plt.show()
all_inputs = df[['sepallength', 'sepalwidth', 'petallength', 'petalwidth']].values
all_classes = df['class'].values

(train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7, random_state=1)
dtc = DecisionTreeClassifier()
dtc.fit(train_inputs, train_classes)
print(dtc.score(test_inputs, test_classes))
plt.show()
#drzewa
iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data,iris.target)
tree.plot_tree(clf.fit(iris.data,iris.target))
dot_data = tree.export_graphviz(clf, out_file=None,
                                feature_names=iris.feature_names,
                                class_names=iris.target_names,
                                filled=True, rounded=True,
                                special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("iris")

iris= load_iris()
X=iris['data']
Y=iris['target']
decision_tree = DecisionTreeClassifier(random_state=0, max_depth=2)
decision_tree=decision_tree.fit(X,Y)
r=export_text(decision_tree,feature_names=iris['feature_names'])
print(r)
