import csv
from Algorithms import bubbleSort

array = [' ']*100
pointer = 0

with open('data4.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    
    next(reader)

    for line in reader:
        array[pointer] = line[0]
        pointer +=1

print(str(array))

            

bubbleSort(array) 

print(str(array))