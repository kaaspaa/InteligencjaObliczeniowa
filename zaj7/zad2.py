# importing the libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, metrics
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA

iris = datasets.load_iris()
y = iris.target
dbscan = DBSCAN()
dbscan.fit(iris.data)
new_labels = dbscan.labels_
print(new_labels)

pca = PCA(n_components=2).fit(iris.data)
pca_2d = pca.transform(iris.data)
for i in range(0, pca_2d.shape[0]):
    if dbscan.labels_[i] == 0:
        c1 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='r', marker='+')
    elif dbscan.labels_[i] == 1:
        c2 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='g', marker='o')
    elif dbscan.labels_[i] == -1:
        c3 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='b', marker='*')
plt.show()

# purity
contingency_matrix = metrics.cluster.contingency_matrix(y,new_labels)
p_score = np.sum(np.amax(contingency_matrix, axis=0)) / np.sum(contingency_matrix)
print("purity wynik:")
print(p_score)

# rand index
ri_score = metrics.adjusted_rand_score(y,new_labels)
print("rand index wynik:")
print(ri_score)
