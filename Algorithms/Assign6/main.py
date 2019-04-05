adjList = {} # adjacency list initialized
INFINITY = 0 # infinity initialized

# code section to read file
with open("nodes.txt","r") as file:
    for line in file:
        x = line.split(" ")
        totalVertices = int(x[0])
        sourceIndex = int(x[1])
        break
    for i in range(totalVertices):
        adjList[i+1] = []
    for line in file:
        x = line.split(" ")
        adjList[int(x[0])].append((int(x[1]), int(x[2])))
        adjList[int(x[1])].append((int(x[0]), int(x[2])))
        INFINITY += int(x[2]) # infinity incremented to reach the total sum of all edges


print("\nSource index =",sourceIndex)
print("\nNumber of vertices =",totalVertices)     

print("\nAdjacency List with weights of each vertex")
for i in range(totalVertices):
    print(" ",i+1," - ",adjList[i+1])

pathLength = [] # array to calculate path length for each vertex
heap = [0] # heap initialized with starting vertex as 0
path = [] # array to track path for each vertex from source

# initialization of the arrays
for i in range(totalVertices):
    pathLength.append(INFINITY)
    if i+1 != sourceIndex:
        heap.append([i+1, INFINITY])
    path.append(sourceIndex)
    
pathLength[sourceIndex-1] = 0
heap[0] = len(heap) # index 0 of heap stores length of heap

# code section to find the min heap by defining functions
def minHeap(heap, index):
    leftIndex = 2*index
    rightIndex = 2*index + 1
    minIndex = index
    
    if leftIndex < len(heap) and heap[leftIndex][1] < heap[minIndex][1]:
        minIndex = leftIndex
        
    if rightIndex < len(heap) and heap[rightIndex][1] < heap[minIndex][1]:
        minIndex = rightIndex
    
    if minIndex != index:
        heap[index], heap[minIndex] = heap[minIndex], heap[index]
        minHeap(heap, minIndex)
                   
def makeHeap(heap):
    for i in range(len(heap)//2,0,-1):
        minHeap(heap, i)   


# code section in which verices linked directly to source are given scores
for i in range(totalVertices):
    for j in range(len(adjList[sourceIndex])):
        if i+1 == adjList[sourceIndex][j][0]:
            heap[i][1] = adjList[sourceIndex][j][1]

makeHeap(heap) # heapifying the heap array

# code section to find the shortest path and path lengths
count = 0
while count < totalVertices - 1:
    heap[1], heap[len(heap)-1] = heap[len(heap)-1], heap[1] # swapping of vertices of smallest weight and last index
    minValue = heap.pop(len(heap)-1) # min weight vertex  pooped out
    heap[0] -= 1 # # heap size decremented
    minHeap(heap, 1) # heapified again
    pathLength[minValue[0]-1] = minValue[1] # path length stored
    
    nextIndex = minValue[0]
    
    # code section to find the shortest path through looping
    for i in range(totalVertices - count - 1):
        for j in range(len(adjList[nextIndex])):
            if i+1 == adjList[nextIndex][j][0]:
                for k in range(heap[0]-1):
                    if heap[k+1][0] == adjList[nextIndex][j][0]:
                        if minValue[1] + adjList[nextIndex][j][1] < heap[k+1][1]:
                            heap[k+1][1] = adjList[nextIndex][j][1] + minValue[1]
                            path[i] = nextIndex # path is stored
    makeHeap(heap)
    count += 1

# code section to display the path of each vertex from source and also path lengths
for i in range(totalVertices):
    if(i!=sourceIndex-1):
        print("\n\nDistance of node",i+1," =",pathLength[i]);
        print("Path = ",i+1, end="")
        j = i
        while True:
            j = path[j] - 1
            print(" <-",j+1, end="")
            if(j == sourceIndex-1):
                break
print("\n")
# +++++++++++++ END OF PROGRAM ++++++++++++++