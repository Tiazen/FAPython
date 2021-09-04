import csv
import random


with open('points.csv', mode='w') as f:
    f_writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for i in range(-500, 501, 5):
        f_writer.writerow([i, random.randint(0, 101)])