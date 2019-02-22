import math

#=============== FUNCTIONS START ===============

# merge function for merge sort algorithm to sort an array
def merge(points, l, m, r, cor):
    # cor is either 0 or 1. When 0, srt along x-axis and when 1, sort along y-axis
    n1 = m - l + 1
    n2 = r - m 
    L = [0] * (n1) 
    R = [0] * (n2) 

    for i in range(0 , n1): 
        L[i] = points[l + i] 

    for j in range(0 , n2): 
        R[j] = points[m + 1 + j] 

    i = 0 
    j = 0  
    k = l  

    while i < n1 and j < n2 : 
        if L[i][cor] <= R[j][cor]: 
            points[k] = L[i] 
            i += 1
        else: 
            points[k] = R[j] 
            j += 1
        k += 1

    while i < n1: 
        points[k] = L[i] 
        i += 1
        k += 1

    while j < n2: 
        points[k] = R[j] 
        j += 1
        k += 1

# mergeSort function for merge sort algorithm to sort an array
def mergeSort(points, l, r, cor): 
    # cor is either 0 or 1. When 0, srt along x-axis and when 1, sort along y-axis
    if l < r: 
        m = int((l+(r-1))/2)
        mergeSort(points, l, m, cor)
        mergeSort(points, m+1, r, cor)
        merge(points, l, m, r, cor)


# Function to find distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Brute Function to find distance between array of 
# pointa used when no. of points less than or equal to 3
def bruteMinDistance(points, noOfPoints): 
    minDist = float("inf") # minDist initialzed to infinity
    for i in range(noOfPoints):
        for j in range(i+1, noOfPoints):
            if ( distance(points[i], points[j]) < minDist ):
                minDist = distance(points[i], points[j])
                pointA = points[i]
                pointB = points[j]
    return [pointA, pointB, minDist]



# Function to find the closest distance between points along y-axis
def closestDistY(points, noOfPoints, minDistList ):
    pointA = minDistList[0]
    pointB = minDistList[1]
    minDist = minDistList[2]
    mergeSort(points, 0, noOfPoints - 1, 1) # points sorted according to y-axis
    for i in range(noOfPoints):
        j = i + 1
        while j < noOfPoints and ( abs(points[i][1] - points[j][1]) < minDist ):
            if(distance(points[i], points[j]) < minDist):
                minDist = distance(points[i], points[j])
                pointA = points[i]
                pointB = points[j]
            j += 1
    return [pointA, pointB, minDist]
            
# function to find the minimum of two values and return the corresponding value and points
def minP(p1, p2):
    if p1[2] < p2[2]:
        return p1
    else:
        return p2

# Recursive function to find the smallest distance
def closestDistance(points, noOfPoints ):
    if noOfPoints <= 3:
        return bruteMinDistance(points, noOfPoints) # finds closest distance by brute force

    mid = int(noOfPoints/2) # index of the mid-point

    dl = closestDistance( points[0:mid], mid) # smallest distance on the left along with the closest points
    dr = closestDistance( points[mid:noOfPoints], noOfPoints - mid) # smallest distance on the right along with the closest points
    minDistList = minP(dl, dr) # Finds the min distance from the left and right along with the closest points

    minDistArray = [] # list to contain the points within min distance
    for i in range(noOfPoints):
        if( abs(points[i][0] - points[mid][0]) < minDistList[2] ): # min distance at index two of minDist
            minDistArray.append(points[i])

    return minP(minDistList, closestDistY(minDistArray, len(minDistArray), minDistList)) 
    # returns minimum of the distance between both sides
    # and also the closest two points

    

#=============== MAIN PROGRAM ===============

db = {} # Dictionaries to store database from the text file

with open("cities.txt","r") as file: # reading the file
    for line in file:
        noOfCities = int(line) # total no of cities
        break
    for line in file:
        x = line.split(", ")
        db[(float(x[1]),float(x[2]))] = x[0] # the cities and the coordinates are stored in a dictionary

points = list(db.keys()) # The coordinates are stored in a list

px = points.copy() # points copied into px
mergeSort(px, 0, noOfCities-1, 0) # px in sorted according to x-axis

pointA, pointB, minDist = closestDistance(px, noOfCities)

print(db[pointA], pointA, "&", db[pointB], pointB, "are the closest with distance %.2f units."%minDist)
