#=============== FUNCTIONS START ===============

# merge function for merge sort algorithm to sort an array
def merge(arr, l, m, r ):
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
        if L[i][1] <= R[j][1]: 
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


#=============== MAIN PROGRAM ===============

db = {} # Dictionary to store values from the text file

with open("values.txt","r") as file: # reading the file
    for line in file:
        x = line.split(" ")
        db[int(x[0])] = (int(x[1]),int(x[2])) # Assignment no and their respective deadline and marks

weightArray = [] # array to store the marks/deadline ratio

for i in range(len(db)):
    weightArray.append(( i+1, db[i+1][0] / db[i+1][1] )) 

mergeSort( weightArray, 0, len(weightArray)-1 )

count = 1
total = 0
result = []
for i in range( len(weightArray) ):
    if( db[weightArray[i][0]][0] >= count ):
        result.append(weightArray[i][0])
        count += 1
        total += db[weightArray[i][0]][1]

print(result)
print("The total marks that'll be obtained is",total)