# FUNCTIONS

# We define a function to check if any sub-array is possible which gives the "sum" by
# adding, subtracting or leaving the elements from the main list
def SubArraySum( arr, endIndex,  sum, answer):
    if sum == 0:
        return True
    elif endIndex >= 0 and answer == False:
        answer = SubArraySum( arr, endIndex-1, sum, answer) # last index ignored
        answer = SubArraySum( arr, endIndex-1, sum - arr[endIndex], answer) # subtracting last index value
        answer = SubArraySum( arr, endIndex-1, sum + arr[endIndex], answer) # adding last index value from main array
    return answer

# MAIN PROGRAM
ListOFElements = ( 3, 6, 2, 4, -1, -7) # The main list from which sum needs to be computed 

answer = False # Answer initialized to false

print("Given List is", ListOFElements)

sum = int(input("\nEnter the sum that needs to be checked "))

N = len(ListOFElements) # Total no of elements in the list

answer = SubArraySum( ListOFElements , N-1, sum, answer)

if answer == True:
    print("\nYes, elements from the main list give the required sum.")
else:
    print("\nNo, no elements of the main list give the required sum.")
