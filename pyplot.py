import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('gpsfile.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    limit = 500
    counter = 0
    for row in plots:
        counter = counter+1
        x.append(float(row[1]))
        y.append(float(row[2]))
        if (counter==limit):
            break


plt.plot(x,y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()