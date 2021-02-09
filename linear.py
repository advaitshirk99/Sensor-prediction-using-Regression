import matplotlib.pyplot as plt 
import numpy as np 
from sklearn import linear_model 
import pandas as pd
from sklearn.linear_model import LinearRegression 

# Load CSV and columns 
df = pd.read_csv("C:\\Users\\tanma\\Downloads\\avg readings.csv") 
   
Y = df['Mean'] 
X = df['Time']

#Reshaping values of X and Y
X=X.values.reshape(len(X),1) 
Y=Y.values.reshape(len(Y),1)

# Fitting Linear Regression to the dataset 

lin = LinearRegression() 
lin.fit(X, Y)
print(lin.predict(X))

print(lin.predict(np.array([[8.0]])))     #predicting values

# Linear Regression results 

plt.scatter(X, Y, color = 'blue')  
plt.plot(X, lin.predict(X), color = 'red') 
plt.title('Linear Regression') 
plt.xlabel('Time in seconds') 
plt.ylabel('Temperature in celsius')   
plt.show()


