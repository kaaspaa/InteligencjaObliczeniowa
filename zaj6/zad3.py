import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
import seaborn as sns
import matplotlib.pyplot as plt
'exec(%matplotlib inline)'

# k-NN
sns.set()
diabetes = pd.read_csv("diabetes.csv")
X_train, X_test, y_train, y_test = train_test_split(diabetes.loc[:, diabetes.columns != 'class'], diabetes['class'],
                                                    stratify=diabetes['class'], test_size=33, train_size=67)
neighbors_settings = [3,5,11]
for n_neighbors in neighbors_settings:
    # build the model
    knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn.fit(X_train, y_train)
    # record test set accuracy
    knn_score = knn.score(X_test, y_test)
    plt.plot(n_neighbors, knn_score, 'bo', label=("knn " + str(n_neighbors)))

# Naive Bayes
X_train, X_test, y_train, y_test = train_test_split(diabetes.loc[:, diabetes.columns != 'class'], diabetes['class'],
                                                    stratify=diabetes['class'], test_size=33, train_size=67)
gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_predict = gnb.predict(X_test)
gnb_score = gnb.score(X_test, y_test)
plt.plot(7, gnb_score, 'ro', label="Gaussian Naive Byes")

# Decision Tree Classifier
X_train, X_test, y_train, y_test = train_test_split(diabetes.loc[:, diabetes.columns != 'class'], diabetes['class'],
                                                    stratify=diabetes['class'], test_size=33, train_size=67)
dtc = DecisionTreeClassifier()
dtc.fit(X_train, y_train)
dtc_score = dtc.score(X_test, y_test)
plt.plot(9, dtc_score, 'go', label="Decision Tree")

# wykres
plt.axis([0,12,0,1])
plt.ylabel("Accuracy")
plt.xlabel("n_neighbors")
plt.legend()
plt.show()
