import matplotlib.pyplot as plt
import csv 

y_points = []

with open('points.csv') as f:
    csv_reader = csv.reader(f, delimiter=';')
    
    for row in csv_reader:
        y_points.append(row[1])

plt.hist(y_points, 10)

plt.show()