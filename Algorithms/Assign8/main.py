A = [9,2,3,8,14,11,12]

Al = []
Ar = []
k = 3

minSum = 0
maxSum = 0

for i in range(len(A)):
    minSum += A[i]

for i in range(len(A)-2):
    Total = 0
    tempArray = []

    for j in range(k):
        Total += A[i+j]
        tempArray.append(A[i+j])

    if Total < minSum:
        minSum = Total
        Al = tempArray.copy()

    elif Total > maxSum:
        maxSum = Total
        Ar = tempArray.copy()

if max(Al) < min(Ar):
    for i in range(len(A)-2):
        tempArray = []
        Total = 0

        for j in range(k):
            Total += A[i+j]
            tempArray.append(A[i+j])
        
        if Al != tempArray:
            if max(tempArray) >= min(Ar):
                Al = tempArray.copy() 
                minSum = Total
                break
                
        if  Ar != tempArray:
            if max(Al) >= min(tempArray):
                Ar = tempArray.copy() 
                maxSum = Total
                break

print("Al = ",Al, "and their sum is", minSum)
print("Ar = ",Ar, "and their sum is", maxSum)
