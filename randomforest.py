import pandas as pd
import numpy as np
import matplotlib.pyplot  as plt
import csv
import seaborn as sns

dataset = pd.read_csv(r"PreProcess/Datasets/Logistic/exp.txt")
print(dataset)
X=dataset.iloc[:,1].values
y=dataset.iloc[:,3].values
print("Complexity",X)
print("Breached",y)

#Splitting the data set into Training and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)
X_train = X_train.reshape(-1, 1)
y_train = y_train.ravel()
X_test=X_test.reshape(-1,1)
print("X TRAIN",X_train)
print("X TEST",X_test)
print("Y TRAIN",y_train)
print("Y TEST",y_test)

#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X= StandardScaler()
X_train =sc_X.fit_transform(X_train)
X_test =sc_X.transform(X_test)

#Fitting the simple linear regression to the training set
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=10,criterion='entropy',random_state = 0)
classifier.fit(X_train, y_train)

# Predicting Test Set Results
y_pred = classifier.predict(X_test)

# making the confusion matrix
#evaluating the model performance
from sklearn.metrics import confusion_matrix,accuracy_score
cm = confusion_matrix(y_test,y_pred)
print("Confusion ",cm)
ac=accuracy_score(y_test, y_pred)
print("Accuracy:",ac)
plt.scatter(X,y,color='red')
plt.xlabel("Complexity")
plt.ylabel("breached/unbreached")
#sns.regplot(x="Complexity",y="Breached", data=dataset, logistic=True,n_boot=500,y_jitter=0.3)
#loss = expit(X_test * classifier.coef_ + classifier.intercept_).ravel()
#plt.plot(X_test, loss, color='black', linewidth=1)
plt.show()

'''
breached=dataset.loc[y==1]
unbreached=dataset.loc[y==0]
print("breached")
print(breached.iloc[:,0])
print(breached.iloc[:,1])
print("Unbreached")
print(unbreached.iloc[:,0])
print(unbreached.iloc[:,1])
plt.scatter(breached.iloc[:,0] , breached.iloc[:,1],s=15,label='breached')
plt.scatter(unbreached.iloc[:,0] , unbreached.iloc[:,1],s=15,label='unbreached')
plt.legend()
plt.show()
'''
'''
# Visualising the Training set results
from matplotlib.colors import ListedColormap
X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('Logistic Regression (Training set)')
plt.xlabel('Complexity')
plt.ylabel('Breached/UnBreached')
plt.legend()
plt.show()

# Visualising the Test set results
from matplotlib.colors import ListedColormap
X_set, y_set = X_test, y_test
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('Classifier (Test set)')
plt.xlabel('Complexity')
plt.ylabel('Breached/UnBreached')
plt.legend()
plt.show()'''