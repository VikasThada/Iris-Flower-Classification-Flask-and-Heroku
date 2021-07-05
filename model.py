
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression


data = pd.read_csv('iris.csv')


variety_mappings = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}


data = data.replace(['Setosa', 'Versicolor' , 'Virginica'],[0, 1, 2])

X = data.iloc[:, 0:-1] 
y = data.iloc[:, -1] 

logreg = LogisticRegression(max_iter=1000) 
logreg.fit(X, y) 


def classify(a, b, c, d):
    arr = np.array([a, b, c, d]) 
    arr = arr.astype(np.float64) 
    query = arr.reshape(1, -1) 
    prediction = variety_mappings[logreg.predict(query)[0]] 
    return prediction 
