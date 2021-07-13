import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

dataset=pd.read_csv("blood-train.csv")
dataset.drop('Number',axis=1,inplace=True)
dataset['target'] = dataset['Made Donation in March 2007']

x=dataset.iloc[:,0:5]
x.drop('Made Donation in March 2007',axis=1,inplace=True)
y=dataset.iloc[:,5]

from sklearn.model_selection import train_test_split

xtrain, xtest, ytrain, ytest = train_test_split(x,y,stratify=y)

from sklearn.neighbors import KNeighborsClassifier
kNN= KNeighborsClassifier(n_neighbors=6, metric = 'minkowski', p=2)

kNN.fit(xtrain,ytrain)

predicted_type = kNN.predict(xtest)

"""from sklearn.metrics import accuracy_score

accuracy_score(ytest,predicted_type)
print("Accuracy is ",accuracy_score(ytest,predicted_type)*100,"%")
"""
#save the model to disk
filename = "finalmodel.sav"
joblib.dump(kNN,filename)


