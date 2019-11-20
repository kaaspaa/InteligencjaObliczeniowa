import classifier as classifier
import pandas as pd
from sklearn.metrics import confusion_matrix
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
                                                    stratify=diabetes['class'], test_size=0.33, train_size=0.67)
neighbors_settings = [3,5,11]
for n_neighbors in neighbors_settings:
    # build the model
    knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn.fit(X_train, y_train)
    # record test set accuracy

    y_pred = knn.predict(X_test)
    knn_score = knn.score(X_test, y_test)
    plt.plot(n_neighbors, knn_score, 'bs', label=("knn " + str(n_neighbors)))
    cm = confusion_matrix(y_test, y_pred)
    print("matrix dla knn " + str(n_neighbors) + " = ")
    print(cm)
    print(knn_score)

# Naive Bayes
X_train, X_test, y_train, y_test = train_test_split(diabetes.loc[:, diabetes.columns != 'class'], diabetes['class'],
                                                    stratify=diabetes['class'], test_size=0.33, train_size=0.67)
gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_predict = gnb.predict(X_test)
gnb_score = gnb.score(X_test, y_test)
plt.plot(7, gnb_score, 'rs', label="Gaussian Naive Byes")
y_pred = gnb.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print("Naive Bayes = ")
print(cm)
print(gnb_score)

# Decision Tree Classifier
X_train, X_test, y_train, y_test = train_test_split(diabetes.loc[:, diabetes.columns != 'class'], diabetes['class'],
                                                    stratify=diabetes['class'], test_size=0.33, train_size=0.67)
dtc = DecisionTreeClassifier()
dtc.fit(X_train, y_train)
dtc_score = dtc.score(X_test, y_test)
plt.plot(9, dtc_score, 'gs', label="Decision Tree")
y_pred = dtc.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print("Decision Tree = ")
print(cm)
print(dtc_score)

# wykres
plt.axis([0,12,0,1])
plt.ylabel("Accuracy")
plt.xlabel("n_neighbors")
plt.legend()
plt.show()
