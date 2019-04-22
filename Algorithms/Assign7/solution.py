#=============== MAIN PROGRAM ===============

assignments = {}    # Dictionary to store deadline and marks 
                    # according to assignment number from the text file

largestDeadline = 1 # we initialize the largest deadline as 1

with open("values.txt","r") as file:    # reading the file
    for line in file:
        x = line.split(" ")
        assignments[int(x[0])] = (int(x[1]),int(x[2]))  # assignment no and  their respective 
                                                        # deadline and marks are added
        if(int(x[1]) > largestDeadline):
            largestDeadline = int(x[1]) # we set largest deadline 

AssignmentOrder = []    # we make an array to store the assignment number and marks

for i in range(largestDeadline):
    AssignmentOrder.append((-1, -1))    # we initialize -1 to both number 
                                        # and marks

for i in range(len(assignments)):
    # we check the index of AssignmentOrder array and if it has (-1 , -1),
    # we replace it with the value from assignments array
    for j in range(assignments[i + 1][0], 0, -1):
        if AssignmentOrder[j - 1][1] == -1:
            AssignmentOrder[j - 1] = (i + 1, assignments[i + 1][1])
            break
    # we check the index of AssignmentOrder array and if it has marks
    # less than that in assignment array, we replace the value in the
    # AssignmentOrder array, else we decrement the AssignmentOrder array
    # index and run the loop again 
        if  assignments[i + 1][1] > AssignmentOrder[j - 1][1]:
            temp = AssignmentOrder[j - 1]
            AssignmentOrder[j - 1] = (i + 1, assignments[i+1][1]) 
            i = temp[0] - 1

totalMarks = 0  # total marks is initialized to zero

print("\n Asgn. no.\t|  Deadline\t|  Marks")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for i in range(len(assignments)):
    print(" ",i+1,"\t\t| ",assignments[i + 1][0],"\t\t| ",assignments[i + 1][1])
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")    

print("\nThe assignments can be done in the order:", end=" ")
for i in range(len(AssignmentOrder)):
    if AssignmentOrder[i] == (-1,-1):
        continue
    else:
        print(AssignmentOrder[i][0], end=" ")
        totalMarks += AssignmentOrder[i][1] # total marks is incremented

print("\n\nThe total marks that'll be obtained is",totalMarks, "\n")