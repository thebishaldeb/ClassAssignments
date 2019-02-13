# Suppose two databases have a collection of movies. Each database has same number of movies which are unique i.e. each database has different set of movies. Now if you query to the database for th Kth movie, it'll return the Kth smallest movie (smallest in terms of duration). Now you need to calculate thr median of the set of two databases of movies




# FUNCTIONS START

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
        if L[i] <= R[j]: 
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
    
    return arr
  
def mergeSort(arr,l,r): 
    if l < r: 
        m = int((l+(r-1))/2)
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        arr = merge(arr, l, m, r)

# FUNCTIONS END 

db1 = []
db2 = []

count = int(input('Enter the nmuber of movies for each data movies: '))

print('Enter the duration for 1st database')
for i in range(count):
    db1.append(int(input()))

print('Enter the duration for 2nd database')
for i in range(count):
    db2.append(int(input()))

print(db1)
print(db2)

mergeSort(db1, 0, count - 1)
mergeSort(db2, 0, count - 1)

print(merge(db1 + db2, 0, count-1, len(db1 + db2)-1))

kth = int(input('\nEnter the no of the smallest movie: '))


print('\nThe reqd. element is ', merge(db1 + db2, 0, count-1, len(db1 + db2)-1)[kth-1])

print("\nThe median of the movies in the two databases is ", merge(db1 + db2, 0, count-1, len(db1 + db2)-1)[int((len(db1 + db2)-1)/2)])

