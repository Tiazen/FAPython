import matplotlib.pyplot as plt
import csv 

x_points = []
y_points = []

with open('points.csv') as f:
    csv_reader = csv.reader(f, delimiter=';')
    
    for row in csv_reader:
        x_points.append(row[0])
        y_points.append(row[1])

plt.plot(x_points, y_points)
plt.show()