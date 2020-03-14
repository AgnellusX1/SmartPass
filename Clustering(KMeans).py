# K-Means Clustering

# Importing Libararies

import numpy as mp
import matplotlib.pyplot as plt
import pandas as pd

# import Datasets
dataset = pd.read_csv("PreProcess/Datasets/Processed/length.txt")
print(dataset)
x = dataset.iloc[:, [2, 1]].values

# Using the elbow Method to find the optimal number of clusters
from sklearn.cluster import KMeans

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

# Plotting the Number of Clusters
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# Applying K-Means to the Dataset
kmeans = KMeans(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=0)
y_kmeans = kmeans.fit_predict(x)
print(y_kmeans)

# Visualising the clusters
plt.scatter(x[y_kmeans == 0, 0], x[y_kmeans == 0, 1], s=100, c='red', label='Very Weak')
plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 1], s=100, c='blue', label='Good')
plt.scatter(x[y_kmeans == 2, 0], x[y_kmeans == 2, 1], s=100, c='green', label='Medium')
plt.scatter(x[y_kmeans == 3, 0], x[y_kmeans == 3, 1], s=100, c='yellow', label='Great')
plt.scatter(kmeans.cluster_centers_[:, 1], kmeans.cluster_centers_[:, 1], s=300, c='black', label='Centroids')
plt.ylabel('Complexity')
plt.xlabel('Length of Passwords')
plt.legend()
plt.show()
