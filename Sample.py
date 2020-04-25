import numpy as np
import random
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


def getTokens(inputString):  # custom tokenizer. ours tokens are characters rather than full words
    tokens = []
    for i in inputString:
        tokens.append(i)
    return tokens


dataset = "Dataset/Complexity3"
data = pd.read_csv(dataset, ',', error_bad_lines=False, encoding='Latin-1')
data = pd.DataFrame(data)
password = np.array(data)

y = [d[1] for d in password]  # labels
allpasswords = [d[0] for d in password]  # actual passwords

vectorizer = TfidfVectorizer(tokenizer=getTokens)  # vectorizing
X = vectorizer.fit_transform(allpasswords)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)  # splitting

lgs = LogisticRegression(penalty='l2', multi_class='ovr')  # our logistic regression classifier
lgs.fit(X_train, y_train)  # training
print(lgs.score(X_test, y_test))  # testing

a = input("Enter the Password to be checked ")
a = [a]
a = vectorizer.transform(a)
b = lgs.predict(a)
print(b)
