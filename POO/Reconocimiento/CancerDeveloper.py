import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale 
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.metrics import (precision_score,
                            accuracy_score,
                            recall_score,
                            f1_score)




def find_TP(y, y_pred):
    return sum((y == 1) & (y_pred == 1))
def find_FP(y, y_pred):
    return sum((y == 0) & (y_pred == 1))
def find_FN(y, y_pred):
    return sum((y == 1) & (y_pred == 0))
def find_TN(y, y_pred):
    return sum((y == 0) & (y_pred == 0))

df = pd.read_csv('POO\Reconocimiento\data.csv')

df = df.drop("id", axis = 1)

df = df.drop("Unnamed: 32", axis = 1)

X = df.loc[:, "radius_mean" : "fractal_dimension_worst"] 
y = df["diagnosis"] 

print(X)
print(y)

y = y.replace({"M" : 1, "B" : 0})

print(y)

X_train, X_test, y_train, y_test = train_test_split(X,y,)

X_train_scaled = scale(X_train)
X_test_scaled = scale(X_test)

svc=SVC() 
svc.fit(X_train_scaled,y_train)
y_pred=svc.predict(X_test_scaled)

print(f'Accuracy Score is {accuracy_score(y_test,y_pred)}')

precision = precision_score(y_test, y_pred)

recall = recall_score(y_test, y_pred)

f1score = 2*((precision*recall)/(precision+recall))

print('Precision: %f' % precision)

print('Recall: %f' % recall)

print('F1 score: %f' % f1score)

print('TP:',find_TP(y_test, y_pred))
print('FN:',find_FN(y_test, y_pred))
print('FP:',find_FP(y_test, y_pred))
print('TN:',find_TN(y_test, y_pred))
