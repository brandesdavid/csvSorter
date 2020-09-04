import csv

f = open('lol.csv', 'r')
b = []
with f:
    reader = csv.reader(f)
    for row in reader:
        for e in row:
            print(e)
            e = b.append

