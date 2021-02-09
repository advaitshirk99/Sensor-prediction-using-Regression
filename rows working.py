import csv
import numpy as np
i=0
j=0
mean=0
meanf=[0,0,0,0,0,0,0,0]
with open("144.csv", "r") as f:
    reader = csv.reader(f, delimiter="\t")
    print(enumerate(reader))
    for i, line in enumerate(reader):
        mean=0
        print('line[{}] = {}'.format(i, line))
        line[0] = eval('[' + line[0] + ']')
        for j in range(1,7):
            mean=mean+line[0][j]
            #print(line[0][])
        meanf[i]=mean/6
        print(meanf[i])
print(meanf)
#while i!=6:
    #print(line0[i])
    #i=i+1
# Data for plotting
t = [5,10,15,20,25,30,35,40]


fig, ax = plt.subplots()
ax.plot(t, meanf)
fig.show()

