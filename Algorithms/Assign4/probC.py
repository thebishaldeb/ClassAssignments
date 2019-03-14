import random

# FUNCTIONS

# Function to generate the list of people who are honest or dishonest with index list as input
def TruthCheck(IndexList, size):
	subList = []
	if size == 1:   
		for i in range(n): # if one element left it checks with the elements of the main list and appends the truth value
			subList.append(honestyCheck(IndexList[0], i))
		return subList
	else:
		if size % 2 != 0:
			lastOddElement = IndexList.pop(-1) # the last element is pooped off and stored here
			size -= 1
		pairs = []
		for i in range(0, size - 1, 2): # pairs are made and stored in the list
			pairs.append((IndexList[i], IndexList[i + 1]))
		for pair in pairs: # we append the first in the pair to a new list 
			if HoneestPair(pair) == True:   
				subList.append(pair[0])
		if len(subList) == 0:      
			subList.append(lastOddElement) # the odd unpaired element is appended
	return TruthCheck(subList, len(subList))

def honestyCheck( A, B): # reply of A about honesty of friend B
	global club
	if club[A] == 1:
		return club[B]
	else:
		return random.choice([ 0, 1])

def HoneestPair(pair): # Checks if both are honest or dishonest
	if honestyCheck(pair[0], pair[1]) == 1 and honestyCheck(pair[1], pair[0]) == 1:
		return True
	else:
		return False 

# MAIN PROGRAM
club = [ 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1]
n = len(club)

IndexList = [] # list to store the index of list club
for i in range(len(club)):
    IndexList.append(i)

TruthList = TruthCheck(IndexList, n) # WE get the list of all the people who are honest and dishonest
print("\t INDEX\t|\tNATURE") 
print("\t-----------------------------")
for i in range(len(TruthList)):
	if TruthList[i] == 1:
		print("\t ", i,"\t|\tHONEST") 
	else:
		print("\t ", i,"\t|\tDISHONEST") 
		
	
