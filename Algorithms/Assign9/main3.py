StringPieces = []   # Array to store the missing pieces
AdjList = {}    # we define an adjacency list to form the graph

with open("MissingPieces.txt", "r") as file:    # missing pieces read from file
    for line in file:
        break
    for line in file:
        # a tuple of message pieces and two flags initialized as 0 is pushed into each index of the array
        # first flag indicates if the string's prefix is similar to another string's prefix or is a substring of another string
        # second flag is used to indicate if the string is already used up
        StringPieces.append([line[:-1], 0, 0])

        # the value of each key (string) is initialized as an empty array
        AdjList[line[:-1]] = []


# ========== FUNCTIONS ==========

# Function to find the postfix-prefix similarity of two strings
def compareStrings(i, j):
    weight = 0  # the weight is initialized to 0
    for k in range(len(StringPieces[i][0])):
        # we run the loop to check letter by letter for prefix-postfix similarity of the two strings
        if StringPieces[j][0][weight] == StringPieces[i][0][k]:
            # condition to tackle letters which repeat in a string like "ee", "aa", etc
            if k+1 < len(StringPieces[i][0]) and StringPieces[j][0][weight] == StringPieces[i][0][k+1] and weight+1 < len(StringPieces[j][0]) and StringPieces[j][0][weight+1] != StringPieces[i][0][k+1]:
                k += 1
                weight = 0
                continue
            weight += 1
            # condition to check if one string is a substring of the other and making the first flag 1
            if weight >= len(StringPieces[j][0]) and k < len(StringPieces[i][0]):
                StringPieces[j][1] = 1
                for m in range(len(AdjList[StringPieces[j][0]])):
                    p = AdjList[StringPieces[j][0]][m][2]
                    StringPieces[p][2] = 0
                weight = 0
                break
        else:
            weight = 0
    if weight > 1:
        # if the weight is more than 1, we append the string piece, weight and the string index of the second string in the AdjList of the first string's value array
        StringPieces[j][2] = 1
        AdjList[StringPieces[i][0]].append((StringPieces[j][0], weight, j))


# Function to find the starting string index of the message
def StartIndexFind():
    for i in range(len(StringPieces)):
        # if the string's prefix doesn't match any prefix or string is not a substring of any other message piece, we take the index
        if StringPieces[i][1] == StringPieces[i][2] == 0:
            index = i
    return index


# Function to find the message from any given index till the end
def MessageDecode(index):
    # message is intialized with string at starting index
    message = StringPieces[index][0]
    # the loop runs until end of string is computed
    while len(AdjList[StringPieces[index][0]]) > 0:
        weight = 0  # the weight is initialized to 0

        # the string piece at the current index position
        curStr = StringPieces[index][0]
        # loop to find the max weighted string for the current string and updating the next index
        for m in range(len(AdjList[curStr])):
            if StringPieces[AdjList[curStr][m][2]][1] == 0 and weight < AdjList[curStr][m][1]:
                weight = AdjList[curStr][m][1]
                index = AdjList[curStr][m][2]

        # message is incrememted to the next string piece
        message += StringPieces[index][0][weight:]
    return message


# ========== MAIN PROGRAM ==========

# loop is run to form the weighted graph of two prefix-postfix pairs
for i in range(len(StringPieces)):
    for j in range(len(StringPieces)):
        if i == j:
            continue
        # function to compare prefix-postfix pairs and form a graph is called
        compareStrings(i, j)

# the function to find the starting string index of the message is called
startIndex = StartIndexFind()

# function to decode the complete message from the pieces is called
decodedMessage = MessageDecode(startIndex)

print("The Message is", decodedMessage)  # the decoded message is printed
