import csv
import numpy
c1 = []
c2 = []
with open('C:\\Users\\tanma\\OneDrive\\Documents\\Project\\144.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        c1.append(row[0])
        c2.append(row[1])
        
for i in range(0, len(c1)): 
    c1[i] = int(c1[i])

for i in range(0, len(c2)): 
    c2[i] = int(c2[i]) 
        
print (str(c1))
print (str(c2)) 

