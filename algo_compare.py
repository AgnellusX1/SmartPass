import pandas as pd
import numpy as np
import matplotlib.pyplot  as plt
dataset = pd.read_csv(r"PreProcess/Datasets/Logistic/exp.txt")
x=dataset.iloc[:,0].values
print(x)
y=dataset.iloc[:,1].values
print(y)
X=[]
for i in range(len(x)):
	X.append(len(x[i]))
print(X)
plt.scatter(X,y,color='red')
plt.xlim(0,20)
plt.xlabel("Length")
plt.ylabel("complexity")
plt.show()
