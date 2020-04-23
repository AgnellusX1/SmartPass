# Importing Libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing Dataset
dataset = pd.read_csv('PreProcess/Datasets/Processed/length4.txt')
x = dataset.iloc[:, [1, 2]].values
print(x)

# # Using the Dendogram to find the Number of Clusters
import scipy.cluster.hierarchy as sch
dendogram=sch.dendrogram(sch.linkage(x,method='ward'))
plt.title("Dendogram")
plt.xlabel("Passwords")
plt.ylabel("Euclidean Distances")
plt.show()

# Fitting Clustering to Dataset
from sklearn.cluster import AgglomerativeClustering
hc=AgglomerativeClustering(n_clusters=4,affinity='euclidean',linkage='ward')
y_hc=hc.fit_predict(x)

# # Visualising the Clusters
plt.scatter(x[y_hc == 0, 0], x[y_hc == 0, 1], s=100, c='red', label='Strong')
plt.scatter(x[y_hc == 1, 0], x[y_hc == 1, 1], s=100, c='blue', label='Week')
plt.scatter(x[y_hc == 2, 0], x[y_hc == 2, 1], s=100, c='green', label='Weakest')
plt.scatter(x[y_hc == 3, 0], x[y_hc == 3, 1], s=100, c='cyan', label='Good')
plt.title('Clusters')
plt.xlabel('Complexity')
plt.ylabel('Length')
plt.legend()
plt.show()
