import csv

f = open('data.csv', 'r')

array = []
pointer = 0

with f:
    reader = csv.reader(f)
    for row in reader:
        for e in row:
          array[pointer] = e
          pointer += 1

def bubbleSort(array):
        length = len(array)-1
        indexminus = 0;
        
        for i in range(length):
            for j in range(0, length-indexminus):
                if array[j] > array[j+1]:
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp

bubbleSort(array) 
