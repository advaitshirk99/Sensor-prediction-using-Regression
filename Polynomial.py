import matplotlib.pyplot as plt 
import numpy as np 
from sklearn import linear_model 
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures 

# Load CSV and columns 
df = pd.read_csv("C:\\Users\\tanma\\Downloads\\avg readings.csv") 
   
Y = df['Mean'] 
X = df['Time']

#Reshaping the values of X and Y
X=X.values.reshape(len(X),1) 
Y=Y.values.reshape(len(Y),1)

poly = PolynomialFeatures(degree = 4) 
X_poly = poly.fit_transform(X)  
poly.fit(X_poly, Y) 
lin2 = LinearRegression() 
lin2.fit(X_poly, Y)

print(lin2.predict(poly.fit_transform(X)))
print("Predicted value = ",lin2.predict(np.array(poly.fit_transform([[8.0]])))) #Predict value at 8 secs

# Visualising the Polynomial Regression results 
plt.scatter(X, Y, color = 'blue')   
plt.plot(X, lin2.predict(poly.fit_transform(X)), color = 'red') 
plt.title('Polynomial Regression') 
plt.xlabel('Time') 
plt.ylabel('Temp') 
  
plt.show()


