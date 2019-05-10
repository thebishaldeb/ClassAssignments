StringPieces = []   # Array to store the missing pieces

with open("MissingPieces.txt", "r") as file:    # missing pieces read from file
    for line in file:
        break
    for line in file:
        StringPieces.append(line[:-1])



# function to merge two strings having similar postfix-prefix groups
def compareStrings(i, j, index):
    count = 0
    for k in range(len(StringPieces[i])):
        # we compare the prefix and postfix of the two strings in loop and increase count
        if StringPieces[j][count] == StringPieces[i][k]:
            # this condition checks for consecutive same letters like "ee", "aa", etc
            if k+1 < len(StringPieces[i]) and StringPieces[j][count] == StringPieces[i][k+1] and StringPieces[j][count+1] != StringPieces[i][k+1]:
                k += 1
                count = 0
                continue
            count += 1
            if count == len(StringPieces[j]):
                # if one string is a complete substring of the other, we pop it out odf the array
                StringPieces.pop(j)
                return index
        else:
            count = 0
    if count > 1:
        # two or more prefix-postfix characters match, we merge the strings into one and store it in one string and pop out the other
        StringPieces[i] = StringPieces[i] + StringPieces[j][count:]
        StringPieces.pop(j)
        return index
    return index+1


def mergeStrings(j):    # function to compare the prefix and postfix of string pieces recursively until the complete string is formed
    if compareStrings(0, j, j) == j or compareStrings(j, 0, j) == j:
         # we compare first the prefix of first string with postfix of another and then vice versa recursively
        if j < len(StringPieces):
            mergeStrings(j)
    else:
        if j+1 < len(StringPieces):
            mergeStrings(j+1)


# MAIN PROGRAM
while len(StringPieces) > 1:
    # the merging of one string piece with another starts from index one
    mergeStrings(1)

message = StringPieces.pop()  # we pop out the string piece that is left in the array

print(message)  # the required message is printed
