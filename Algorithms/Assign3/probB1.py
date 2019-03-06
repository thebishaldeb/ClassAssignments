# FUNCTIONS
def partition(arr, low, high):
    i = 0
    apple_to_compare = 0
    while i < len(A):
        if TightFit(i, arr[high]) == 0:
            apple_to_compare = i
            break
        i+=1
    i = low
    pivot = low - 1
    while i < high:
        if TightFit(apple_to_compare, arr[i]) >= 0:
            pivot+=1
            arr[i], arr[pivot] = arr[pivot], arr[i]
        i+=1
    arr[i], arr[pivot + 1] = arr[pivot + 1], arr[i]
    return pivot + 1

# Function to do Quick sort 
def quickSort( arr, low, high): 
    if low < high: 
        pi = partition( arr, low, high) 
        quickSort( arr, low, pi-1) 
        quickSort( arr, pi+1, high) 

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

quickSort( M, 0, len(M)-1)

# Tabular display
print("\t", "i", "\t|\t", "P[i]", "\t|\t",  "A[i]", "\t|\t", "M[i]", "\t|\t", "P[M[i]]" )
print("\t-------------------------------------------------------------------------")
for i in range(len(A)):
    print("\t", i, "\t|\t", P[i], "\t|\t", A[i], "\t|\t", M[i], "\t|\t", P[M[i]] )









