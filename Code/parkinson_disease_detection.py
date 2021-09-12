# -*- coding: utf-8 -*-
"""Parkinson_Disease_Detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hhBNB3LOoWr016Knaxr_lWzgVX-Hc7PO

## Importing Necessary Python Libraries
"""

import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.metrics import accuracy_score
print("Libraries imported")

"""## Dataset """

parkinson_data = pd.read_csv("parkinsons.csv")
parkinson_data.head(10) #printing first 10 rows of dataframe

parkinson_data.shape #rows and columns in dataset

parkinson_data.describe() #statistical data about the dataset

parkinson_data.isnull().sum() #checking for missing values

parkinson_data.info() #getting more info about the dataset

parkinson_data.corr()

plt.figure(figsize=(25, 25))
p = sns.heatmap(parkinson_data.corr(), annot=True)

# target variable = status 
parkinson_data['status'].value_counts()

"""##### 0 --> Without Parkinson; 1 --> Parikson Positive

## Grouping data based on target variable
"""

parkinson_data.groupby('status').mean()

"""## Data Pre-Processing

#### Seperating Features and Target variables
"""

X = parkinson_data.drop(columns=['status','name'], axis=1) #dropping column axis = 1; dropping row then axis = 0
Y = parkinson_data['status']

print(X)

print(Y)

"""#### Splitting the data into testing and training set"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""## Data Standardization"""

scaler = StandardScaler()

scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

print(X_train)

"""## Model Training

### Using Support Vector Machine
"""

model = svm.SVC(kernel='linear')

# training the SVM model with training data
model.fit(X_train, Y_train)

"""## Model Evaluation

#### Accuracy Score
"""

# Accuracy Score on training data
X_train_pred = model.predict(X_train)
training_data_accuracy = accuracy_score(Y_train, X_train_pred)

print('Accuracy (Training Data) :', training_data_accuracy*100, '%')

# Accuracy Score on test data
X_test_pred = model.predict(X_test)
testing_data_accuracy = accuracy_score(Y_test, X_test_pred)

print('Accuracy (Testing Data) :', testing_data_accuracy*100, '%')

"""## Predictive System"""

#input_data = (95.730,132.068,91.754,0.00551,0.00006,0.00293,0.00332,0.00880,0.02093,0.191,0.01073,0.01277,0.01717,0.03218,0.01070,21.812,0.615551,0.773587,-5.498678,0.327769,2.322511,0.231571)
input_data = (197.07600,206.89600,192.05500,0.00289,0.00001,0.00166,0.00168,0.00498,0.01098,0.09700,0.00563,0.00680,0.00802,0.01689,0.00339,26.77500,0.422229,0.741367,-7.348300,0.177551,1.743867,0.085569)

# changing input data to numpy array
input_data_numpy = np.asarray(input_data)

#reshaping the numpy array 
input_data_reshape = input_data_numpy.reshape(1,-1)

#standardizing the input data 
std_data = scaler.transform(input_data_reshape)

## prediction
prediction = model.predict(std_data)
print(prediction)

if (prediction[0] == 1):
  print('The patient has Parkinson')
elif (prediction[0] == 0):
  print('The patient does not have Parkinson')
else:
  print('Some error in processing')

"""## Extracting the ML Model

#### Using Pickle
"""

import pickle

with open('model_pickle','wb') as f:
  pickle.dump(model,f)

with open('model_pickle','rb') as f:
  mp = pickle.load(f) #loading the made model

"""#### Testing the working of model """

input_data = (95.730,132.068,91.754,0.00551,0.00006,0.00293,0.00332,0.00880,0.02093,0.191,0.01073,0.01277,0.01717,0.03218,0.01070,21.812,0.615551,0.773587,-5.498678,0.327769,2.322511,0.231571)
input_data_numpy = np.asarray(input_data)

#reshaping the numpy array 
input_data_reshape = input_data_numpy.reshape(1,-1)

#standardizing the input data 
std_data = scaler.transform(input_data_reshape)

## prediction
prediction = mp.predict(std_data) #model made using Pickle
print(prediction)

"""#### Using Sklearn Joblib"""

from sklearn.externals import joblib

joblib.dump(model,'model-joblib')

mj = joblib.load('model-joblib') #loading the model

"""#### Testing the working of model"""

input_data = (95.730,132.068,91.754,0.00551,0.00006,0.00293,0.00332,0.00880,0.02093,0.191,0.01073,0.01277,0.01717,0.03218,0.01070,21.812,0.615551,0.773587,-5.498678,0.327769,2.322511,0.231571)
input_data_numpy = np.asarray(input_data)

#reshaping the numpy array 
input_data_reshape = input_data_numpy.reshape(1,-1)

#standardizing the input data 
std_data = scaler.transform(input_data_reshape)

## prediction
prediction = mj.predict(std_data)  #model made using joblib
print(prediction)