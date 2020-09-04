import csv

f = open('lol.csv', 'r')
b = []
i = 0

with f:
    reader = csv.reader(f)
    for row in reader:
        for e in row:
            b[i] = e
            i += 1

          
for x in b:
  print(b[x])

def bubbleSort(array):
        length = len(array)-1
        indexminus = 0;
        
        for i in range(length):
            for j in range(0, length-indexminus):
                if array[j] > array[j+1]:
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp

bubbleSort(b) 

for i in range(len(b)): 
    print ("%d" %b[i])