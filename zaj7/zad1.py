# importing the libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn import  metrics

iris = datasets.load_iris()
# 1
X = iris.data[:, :2]
y = iris.target
km = KMeans(n_clusters=3, n_jobs=4, random_state=21)
km.fit(X)
centers = km.cluster_centers_
print(centers)
new_labels = km.labels_
# Plot the identified clusters and compare with the answers
fig, axes = plt.subplots(1, 2, figsize=(16,8))
axes[0].scatter(X[:, 0], X[:, 1], c=y, cmap='gist_rainbow',edgecolor='k', s=150)
axes[1].scatter(X[:, 0], X[:, 1], c=new_labels, cmap='jet',edgecolor='k', s=150)
axes[0].set_xlabel('Sepal length', fontsize=18)
axes[0].set_ylabel('Sepal width', fontsize=18)
axes[1].set_xlabel('Sepal length', fontsize=18)
axes[1].set_ylabel('Sepal width', fontsize=18)
axes[0].tick_params(direction='in', length=10, width=5, colors='k', labelsize=20)
axes[1].tick_params(direction='in', length=10, width=5, colors='k', labelsize=20)
axes[0].set_title('Actual', fontsize=18)
axes[1].set_title('Predicted', fontsize=18)
plt.show()
print("y:")
print(y)
print("new:")
print(new_labels)

# purity
contingency_matrix = metrics.cluster.contingency_matrix(y,new_labels)
p_score = np.sum(np.amax(contingency_matrix)) / np.sum(contingency_matrix)
print("purity wynik:")
print(p_score)

# rand index
ri_score = metrics.adjusted_rand_score(y, new_labels)
print("rand index wynik")
print(ri_score)
