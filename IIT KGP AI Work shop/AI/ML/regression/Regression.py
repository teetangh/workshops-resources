#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 08:22:56 2019

@author: rohans
"""

import numpy as np
import matplotlib.pyplot as plot
import pandas as pd

# Import the dataset
dataset = pd.read_csv('salary.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

from sklearn.linear_model import LinearRegression
linearRegressor = LinearRegression()
linearRegressor.fit(X_train, y_train)
y_pred = linearRegressor.predict(X_test)

plot.scatter(X_train, y_train, color = 'red')
plot.plot(X_train, linearRegressor.predict(X_train), color = 'blue')
plot.title('Salary vs Experience (Training set)')
plot.xlabel('Years of Experience')
plot.ylabel('Salary')
plot.show()

plot.scatter(X_test, y_test, color = 'red')
plot.plot(X_train, linearRegressor.predict(X_train), color = 'blue')
plot.title('Salary vs Experience (Test set)')
plot.xlabel('Years of Experience')
plot.ylabel('Salary')
plot.show()
