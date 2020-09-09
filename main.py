import csv
from Algorithms import *

sortingAlgorithm = input("what sorting algorithm do you want to use? (bubbleSort, insertionSort, selectionSort): ")

fileName = input("what is the file name? (csv): ")
dataName = fileName + ".csv"

size = int(input("how many numbers does your file have?: "))

array = [' ']*size
pointer = 0



with open(dataName, 'r') as csv_file:
    reader = csv.reader(csv_file)
    
    next(reader) # skips first line of csv

    for line in reader:
        array[pointer] = line[0]
        pointer +=1


if(sortingAlgorithm.upper == "BUBBLESORT"):
  bubbleSort(array)
elif(sortingAlgorithm.upper == "INSERTIONSORT"):
  insertionSort(array)
else: 
  selectionSort(array)

for x in array:
    print(x, end=" ")
            
