# -*- coding: utf-8 -*-
"""salary-prediction-simple-linear-regression-eda.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h0lFjqZJWrrj1LkGRzD6na6_c3yDU8GS
"""

# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All"
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

"""# **IMPORTING THE REQUIRED LIBRARIES**"""

import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

"""# **LOADING THE DATASET**"""

df=pd.read_csv("sari_roti.csv")
df

#Checking for null values
df.isnull().any()

"""# **EXPLORATORY DATA ANALYSIS**"""

fig = px.scatter(df, y="Salary", x="YearsExperience", color="YearsExperience")
fig.update_traces(marker_size=8)

fig, ax = plt.subplots(figsize =(10, 5))
ax.hist(df["YearsExperience"],color='#FDE992',ec="#50C878", lw=3)
plt.title('Experience Distribution')
plt.xlabel('Experience Years')
plt.show()

fig, ax = plt.subplots(figsize =(10, 5))
ax.hist(df["Salary"],color='#F9E076',ec="#8F00FF", lw=2)
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.show()

plt.figure(figsize=[3,3])
sns.heatmap(df.corr(),annot=True)

"""**From the EDA, we can infer that:**

1) Years of Experience and Salary are highly correlated to each other.

2) As years of experience increases, salary also increases.

# **SPLITTING INTO DEPENDENT AND INDEPENDENT VARIABLES**
"""

#Dependent variable
y=df['Salary']

#Independent variable
X=df.drop(columns='Salary',axis=1)
X.head()

"""# **SPLITTING INTO TRAIN AND TEST DATA**"""

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=0)

"""# **SIMPLE LINEAR REGRESSION**"""

from sklearn.linear_model import LinearRegression
model=LinearRegression() # initialzing the model
model.fit(X_train,y_train) # fitting the model on training data

"""# **TESTING THE MODEL**"""

y_pred=model.predict(X_test)

"""# **EVALUATION METRICS**"""

from sklearn import metrics

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
rmse = np.sqrt(metrics.mean_squared_error(y_test, y_pred))

from sklearn.metrics import r2_score
r2_score(y_test, y_pred)

"""# **PLOTTING PREDICTED VALUES AND ACTUAL VALUES**"""

plt.figure(figsize=(6,6))
plt.scatter(y_test, y_pred, c='crimson')
plt.yscale('log')
plt.xscale('log')

p1 = max(max(y_pred), max(y_test))
p2 = min(min(y_pred), min(y_test))
plt.plot([p1, p2], [p1, p2], 'b-')
plt.xlabel('True Values', fontsize=15)
plt.ylabel('Predictions', fontsize=15)
plt.axis('equal')
plt.show()

# Plotting the actual and predicted values

c = [i for i in range (1,len(y_test)+1,1)]
plt.plot(c,y_test,color='r',linestyle='-')
plt.plot(c,y_pred,color='b',linestyle='-')
plt.xlabel('Salary')
plt.ylabel('index')
plt.title('Prediction')
plt.show()

# plotting the error
c = [i for i in range(1,len(y_test)+1,1)]
plt.plot(c,y_test-y_pred,color='green',linestyle='-')
plt.xlabel('index')
plt.ylabel('Error')
plt.title('Error Value')
plt.show()