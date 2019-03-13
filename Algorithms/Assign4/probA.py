# check function to check is a subset is possible to create Z by the addition or subtraction of 
# its elements
# we check if leaving, adding , or subtracting the last element of the set 
# on each recursive call can generate us the given integer Z
# we make z = z if last element is left
# z=z+last element , if last element is subtracted
# z=z-last element ,	if last element is added
# hence we seek if Z is zero or not

# FUNCTIONS

def SubArraySum( arr, endIndex,  sum, answer):
    if sum == 0:
        return True
    elif endIndex >= 0 and answer == False:
		# leaving last index
        answer = SubArraySum( arr, endIndex-1, sum, answer)
		# subtracting last index
        answer = SubArraySum( arr, endIndex-1, sum - arr[endIndex], answer)
	 	# adding last index
        answer = SubArraySum( arr, endIndex-1, sum + arr[endIndex], answer)
    return answer

# MAIN PROGRAM
ListOFElements = ( 3, 6, 2, 4, -1, -7) # The main list from which sum needs to be computed 

answer = False # Answer initialized to false

print("Given List is", ListOFElements)

sum = int(input("\nEnter the sum to be checked "))

N = len(ListOFElements) # Total no of elements in the list

answer = SubArraySum( ListOFElements , N-1, sum, answer)

if answer == True:
    print("\nYes, such a subset will exist")
else:
    print("\nNo, such a subset doesn't exist")
