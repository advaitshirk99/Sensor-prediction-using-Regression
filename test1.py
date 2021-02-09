import matplotlib.pyplot as plt
import numpy as np
import csv
  
def estimate_coef(x, y): 
    # number of observations/points 
    n = np.size(x) 
  
    # mean of x and y vector 
    m_x, m_y = np.mean(x), np.mean(y) 
  
    # calculating cross-deviation and deviation about x 
    SS_xy = np.sum(y*x) - n*m_y*m_x 
    SS_xx = np.sum(x*x) - n*m_x*m_x 
  
    # calculating regression coefficients 
    b_1 = SS_xy / SS_xx 
    b_0 = m_y - b_1*m_x 
  
    return(b_0, b_1) 
  
def plot_regression_line(x, y, b): 
    # plotting the actual points as scatter plot 
    plt.scatter(x, y, color = "m", 
               marker = "o", s = 30) 
  
    # predicted response vector 
    y_pred = b[0] + b[1]*x 
  
    # plotting the regression line 
    plt.plot(x, y_pred, color = "g") 
  
    # putting labels 
    plt.xlabel('x') 
    plt.ylabel('y') 
  
    # function to show plot 
    plt.show() 
  
def main():
    x = []
    y = []
    with open('C:\\Users\\tanma\\OneDrive\\Documents\\Project\\144.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            x.append(row[0])
            y.append(row[1])
        for i in range(0, len(x)):
            x[i] = int(x[i])
        for i in range(0, len(y)):
            y[i] = int(y[i]) 
      
    # estimating coefficients 
    b = estimate_coef(x, y) 
    print("""Estimated coefficients:\nb_0 = {}  \ 
          \nb_1 = {}""".format(b[0], b[1])) 
  
    # plotting regression line 
    plot_regression_line(x, y, b) 
  
if __name__ == "__main__": 
    main() 
