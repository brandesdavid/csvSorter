import csv
from Algorithms import bubbleSort, insertionSort

array = [' ']*100
pointer = 0

with open('data4.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    
    next(reader) # skips first line of csv

    for line in reader:
        array[pointer] = line[0]
        pointer +=1


insertionSort(array)

for x in array:
    print(x)
            
