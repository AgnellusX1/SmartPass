# K-Means Clustering

def passrun():
    distances = []

    password = input("Enter the Password to be Tested")
    pass_len = len(password)
    from password_strength import PasswordStats

    pass_complex = PasswordStats(password).strength()

    from scipy.spatial import distance

    for i in range(kmeans.n_clusters):
        p1 = (kmeans.cluster_centers_[i])
        # print(p1)
        p2 = (pass_len, pass_complex)
        d = distance.euclidean(p1, p2)
        distances.append(d)

    # print(distances)
    clus_names = ['Very Week', 'Good', 'Week', 'Best']
    low = distances.index(min(distances))
    target_cluster = kmeans.cluster_centers_[low]
    # print(target_cluster)
    # print(low)
    print("Your Password Belong to the Category of")
    print(clus_names[low])

    # Visualising the clusters
    # plt.scatter(x[y_kmeans == 0, 0], x[y_kmeans == 0, 1], s=100, c='red', label='Very Weak')
    # plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 1], s=100, c='orange', label='Good')
    # plt.scatter(x[y_kmeans == 2, 0], x[y_kmeans == 2, 1], s=100, c='blue', label='Week')
    # plt.scatter(x[y_kmeans == 3, 0], x[y_kmeans == 3, 1], s=100, c='green', label='Great')
    plt.scatter(pass_len, pass_complex, c='pink', label='Your Password', s=300)
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='black', label='Centroids')
    plt.ylabel('Complexity')
    plt.xlabel('Length of Passwords')
    plt.legend()
    plt.show()

    ans = input("Try a new Password??  Y  or   N ")
    if ans == 'Y':
        passrun()


# Importing Libararies

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

# import Datasets
dataset = pd.read_csv("PreProcess/Datasets/Processed/length.txt")
# print(dataset)
x = dataset.iloc[:, [2, 1]].values

# Using the elbow Method to find the optimal number of clusters
from sklearn.cluster import KMeans

# wcss = []
# for i in range(1, 11):
#     kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
#     kmeans.fit(x)
#     wcss.append(kmeans.inertia_)
#
# # Plotting the Number of Clusters
# plt.plot(range(1, 11), wcss)
# plt.title('The Elbow Method')
# plt.xlabel('Number of Clusters')
# plt.ylabel('WCSS')
# plt.show()

# Applying K-Means to the Dataset
kmeans = KMeans(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=0)
kmeans.fit(x)
pickle.dump(kmeans, open("model1.pkl", 'wb'))
y_kmeans = kmeans.fit_predict(x)
# print(y_kmeans)
# print(kmeans.labels_)
# clust = kmeans.labels_.tolist()
# cus1 = []
# cus2 = []
# cus3 = []
# cus4 = []
# print(clust)
# for i in (clust):
#     if i == 0:
#         cus1.append(dataset.iloc[i:1].values)
#         print(dataset.iloc[i:1].values)
#     elif i == 1:
#         cus2.append(dataset.iloc[i:1].values)
#     elif i == 2:
#         cus3.append(dataset.iloc[i:1].values)
#     elif i == 3:
#         cus4.append(dataset.iloc[i:1].values)
# print(cus1, cus2, cus3, cus4)
# for i in range(kmeans.n_clusters):
#     var = {i: np.where(kmeans.labels_ == i)[0]}
#     print(var)
# print(kmeans.cluster_centers_)
var = {i: np.where(kmeans.labels_ == i)[0] for i in range(kmeans.n_clusters)}
# print(var)
passrun()
