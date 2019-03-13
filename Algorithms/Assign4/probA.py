# FUNCTIONS

# We define a function to check if any sub-array is possible which gives the "Z" by
# adding, subtracting or leaving the elements from the main list
def _isSummable( arr, endIndex, Z, answer):
    if Z == 0:
        return True
    elif endIndex >= 0 and answer == False:
        answer = _isSummable( arr, endIndex-1, Z, answer) # last index ignored
        answer = _isSummable( arr, endIndex-1, Z - arr[endIndex], answer) # subtracting last index value
        answer = _isSummable( arr, endIndex-1, Z + arr[endIndex], answer) # adding last index value from main array
    return answer

# IsSummable(Z, A) from the problem statement
def isSummable( Z, A):
    N = len(A) # Total no of elements in the list
    answer = False # Answer initialized to false
    answer = _isSummable( A , N-1, Z, answer)
    if answer == True:
        print("\nYes, it is possible to find a subset from the main set which gives the required value of Z.")
    else:
        print("\nNo, it is not possible to find a subset from the main set which gives the required value of Z.")

# MAIN PROGRAM
A = ( 3, 6, 2, 4, -1, -7) # The main list from which sum needs to be computed 

print("Given List is", A)

Z = int(input("\nEnter the value of Z that needs to be checked "))

isSummable( Z, A) # The function to check the required condition

