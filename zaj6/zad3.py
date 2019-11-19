import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
import seaborn as sns
import matplotlib.pyplot as plt
'exec(%matplotlib inline)'

#k-NN
sns.set()
diabetes = pd.read_csv("diabetes.csv")
X_train, X_test, y_train, y_test = train_test_split(diabetes.loc[:, diabetes.columns != 'class'], diabetes['class'],
                                                    stratify=diabetes['class'], test_size=33, train_size=67)
training_accuracy = []
test_accuracy = []
# try n_neighbors from 1 to 10
neighbors_settings = [3,5,11]
for n_neighbors in neighbors_settings:
    # build the model
    knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn.fit(X_train, y_train)
    # record training set accuracy
    training_accuracy.append(knn.score(X_train, y_train))
    # record test set accuracy
    test_accuracy.append(knn.score(X_test, y_test))
plt.plot(neighbors_settings, training_accuracy, 'ro', label="training accuracy")
plt.plot(neighbors_settings, test_accuracy, 'bo', label="test accuracy")
plt.axis([0,12,0,1])
plt.ylabel("Accuracy")
plt.xlabel("n_neighbors")
plt.legend()
#plt.show()

#Naive Bayes
X_train, X_test, y_train, y_test = train_test_split(diabetes.loc[:, diabetes.columns != 'class'], diabetes['class'],
                                                    stratify=diabetes['class'], test_size=33, train_size=67)
gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_predict = gnb.predict(X_test)
print("Poprawnosc Gaussian naive bytes: {:.2f}".format(gnb.score(X_test, y_test)))

#drzewo decyzyjne
