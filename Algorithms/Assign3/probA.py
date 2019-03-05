# merge function for merge sort algorithm to sort an array
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m 
    L = [0] * (n1) 
    R = [0] * (n2) 

    for i in range(0 , n1): 
        L[i] = arr[l + i] 

    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 

    i = 0 
    j = 0
    k = l  

    while i < n1 and j < n2 : 
        if IsLargeApples( L[i], R[j]) == -1: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
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
        m = int((l+(r-1))/2)
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

# IsLargeApples( i, j) function
def IsLargeApples(i,j):
    if(A[i]>A[j]): # Checks wheter Apple i is bigger or j
        return 1
    else:
        return -1


# MAIN PROGRAM 

# List of Apples of different sizes stored in tuple to avoid changes
A = (87, 24, 32, 20, 91, 50, 52, 6, 9, 23, 37, 90, 48, 75, 22, 7, 13, 77, 56, 60, 1, 4, 28, 57, 35, 41, 63, 88, 40, 8)

S = [] # List to store indices

for i in range(len(A)):
    S.append(i)

print("List of Apples of different sizes: ", A)

mergeSort(S, 0, len(S)-1)

print("List of Indices sorted according to apple size:: ", S)