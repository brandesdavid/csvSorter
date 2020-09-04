import csv

f = open('data.csv', 'r')

array = [' ']*10
pointer = 0

with f:
    reader = csv.reader(f)
    for row in reader:
        for e in row:
          array[pointer] = int(e)
          pointer += 1

print(str(array))

def bubbleSort(arr):
    n = len(arr) 
  
    
    for i in range(n-1):
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]
            

bubbleSort(array) 

print(str(array))