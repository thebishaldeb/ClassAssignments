# merge function for merge sort algorithm to sort an array
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m 
    L = [0] * (n1) 
    R = [0] * (n2) 

    k = 0
    for i in range( l, m+1): 
        L[k] = arr[i] 
        k += 1

    k = 0
    for j in range( m+1, r+1): 
        R[k] = arr[j] 
        k += 1

    i = 0 
    j = 0
    k = l  

    while i < n1 and j < n2 :
        var1 = 0
        var2 = 0
        while var1 < size:
            if TightFit( var1, L[i]) == 0:
                break
            var1 += 1
        while var2 < size:
            if TightFit( var2, R[j]) == 0:
                break
            var2 += 1
        if var1 < var2:
            arr[k]=L[i]
            i += 1
        else:
            arr[k]=R[j]
            j += 1
        k += 1
            
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1

    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1

# mergeSort function for merge sort algorithm to sort an array
def mergeSort(arr, l, r): 
    if l < r: 
        m = l + int((r-l)/2)
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

# TightFit function from the question
def TightFit( i, j):
    if A[i] == P[j]:
        return 0
    elif A[i] > P[j]:
        return -1
    else:
        return 1



## MAIN PROGRAM =======================================

# List of Apples of different sizes stored in tuple to avoid changes
A = (87, 24, 32, 20, 91, 50, 52, 6, 9, 23, 37, 90, 48, 75, 22, 7, 13, 77, 56, 60, 1, 4, 28, 57, 35, 41, 63, 88, 40, 8)

# List of Packets stored in a tuple to avoid making changes
P = (37, 23, 4, 40, 9, 20, 48, 28, 56, 22, 24, 90, 7, 60, 52, 63, 50, 1, 32, 87, 77, 6, 91, 13, 35, 41, 57, 8, 75, 88)

M = [] # List to store indices

for i in range(len(A)):
    M.append(i)

size = len(M)

mergeSort( M, 0, size-1) # Sorting the indices of M using mergesort

# Tabular display
print("\t", "i", "\t|\t", "P[i]", "\t|\t",  "A[i]", "\t|\t", "M[i]", "\t|\t", "P[M[i]]" )
print("\t-------------------------------------------------------------------------")
for i in range(len(A)):
    print("\t", i, "\t|\t", P[i], "\t|\t", A[i], "\t|\t", M[i], "\t|\t", P[M[i]] )
