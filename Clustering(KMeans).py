# K-Means Clustering

# Importing Libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.cluster import KMeans
from password_strength import PasswordStats
from scipy.spatial import distance


def passrun():
    distances = []

    password = input("Enter the Password to be Tested ")
    pass_len = len(password)
    pass_complex = PasswordStats(password).strength()

    for i in range(kmeans.n_clusters):
        p1 = (kmeans.cluster_centers_[i])
        p2 = (pass_len, pass_complex)
        d = distance.euclidean(p1, p2)
        distances.append(d)

    # print(distances)
    clus_names = ['Highly Breachable', 'Partially Unbreachable', 'Partially Breachable', 'Highly UnBreachable']
    low = distances.index(min(distances))
    print("Your Password Belong to the Category of ")
    print(clus_names[low])

    # Visualising the clusters
    plt.scatter(x[y_kmeans == 0, 0], x[y_kmeans == 0, 1], s=100, c='red', label='Very Weak')
    plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 1], s=100, c='orange', label='Good')
    plt.scatter(x[y_kmeans == 2, 0], x[y_kmeans == 2, 1], s=100, c='blue', label='Week')
    plt.scatter(x[y_kmeans == 3, 0], x[y_kmeans == 3, 1], s=100, c='green', label='Great')
    plt.scatter(pass_len, pass_complex, c='pink', label='Your Password', s=300)
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='black', label='Centroids')
    plt.ylabel('Complexity')
    plt.xlabel('Length of Passwords')
    plt.legend()
    plt.show()

    ans = input("Try a new Password??  Y  or   N ")
    if ans == 'Y':
        passrun()


# import Datasets
dataset = pd.read_csv("PreProcess/Datasets/Processed/length.txt")
print(dataset)
x = dataset.iloc[:, [2, 1]].values

# Using the elbow Method to find the optimal number of clusters
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
kmeans.fit(x)
pickle.dump(kmeans, open("model1.pkl", 'wb'))
y_kmeans = kmeans.fit_predict(x)
print(kmeans.labels_)
print(kmeans.cluster_centers_)
var = {i: np.where(kmeans.labels_ == i)[0] for i in range(kmeans.n_clusters)}
print(var)
passrun()
