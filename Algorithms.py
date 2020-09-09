def bubbleSort(arr):
    n = len(arr) 
  
    
    for i in range(n-1):
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selectionSort(liste):
    n = len(liste)
    for i in range(n-1):
        minSort = i
        for j in range(i, n):
            if(liste[minSort] > liste[j]):
                minSort = j
                tmp = liste[i]
                liste[i] = liste[minSort]
                liste[minSort] = tmp

def insertionSort(liste):
    for a in range(1,len(liste)):
        
        temp = liste[a]
        b = a-1
        
        while(b>=0 and temp < liste[b]):
            liste[b+1] = liste[b]
            b -= 1
        liste[b+1] = temp

  