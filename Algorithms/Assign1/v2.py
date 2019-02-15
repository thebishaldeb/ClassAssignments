# FUNCTION

def med(arr1, arr2, length):
    
    if length == 2:
        return findMed( arr1, arr2)
    
    mid = int((length-1)/2)

    if (arr1[mid] < arr2[mid]):
        return med( arr2[0:mid+1], arr1[-mid-1:length], len(arr2[0:mid+1]))
    
    elif (arr1[mid] > arr2[mid]):
        return med( arr1[0:mid+1], arr2[-mid-1:length], len(arr1[0:mid+1]))

def findMed(arr1, arr2):
    return sorted(arr1 + arr2)[int(len(arr1 + arr2)/2 - 1)]     
    

# Dictionaries to store databases from the text files
db1 = {}
db2 = {}

with open("db1.txt","r") as file:
    for line in file:
            x = line.split("- ")
            db1[int(x[0])] = x[1][0:len(x[1])-1]


with open("db2.txt","r") as file:
    for line in file:
            x = line.split("- ")
            db2[int(x[0])] = x[1][0:len(x[1])-1]

print(db1)
print(db2)

kth = int(input('\nEnter the no of the smallest movie: '))

print('\nThe reqd. smallest movie from first database:', db1[sorted(db1)[kth-1]])
print('\nThe reqd. smallest movie from second database:', db2[sorted(db2)[kth-1]])

# The Duration of the movie of Databases sorted and stored in the lists
arr1 = sorted(db1)
arr2 = sorted(db2)

length = len(arr1) # No. of movies in the database


median = med(arr1, arr2, length) #Function 'med' defined at the top.

for i in range(length):
    if arr1[i] == median:
        print("\nThe movie with median duration, i.e.",median, "is", db1[median])
        break
    elif arr2[i] == median:
        print("\nThe movie with median duration, i.e.",median, "is", db2[median])
        break
        