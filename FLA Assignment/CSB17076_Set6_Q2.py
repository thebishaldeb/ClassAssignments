# Roll No - CSB17076

# ============ FUNCTIONS ============

# function to check if the string is valid in the language
def PDA_validation(InputString):
    stack = ["z"]   # we initialize a stack with z as the top element

    # We define three states: 0, 1 & 2
    # State 0 is when "0" is pushed into stack
    # State 1 is when "0" is popped out of stack
    # State 2 is the final state when the stack is empty and end of input string 
    # The string is accepted if it reaches state 2 at the end.
    state = 0   # start state is 0

    i = 0

    while(InputString[i]!="~"): # "~" indicates "\0"

        # condition when input is "0"
        if InputString[i]=="0":
            
            if stack[-1] != "z": 
                # we enter function to check the validation by popping from the stack 
                # and going to next state
                state = NextState(InputString, i, state, stack) 
                
            # if the state is 0 even after previous condition, "0" is pushed into the stack
            if state == 0: 
                stack.append("0")   # check the validation by pushing into stack
                i += 1
            else:
                break   # if the state is not 0, we break from the while loop 
        
        # condition when input is "0"
        elif InputString[i]=="1":

                # the state goes to 1 and 
                # one "0" is popped out from top of the stack
                if stack[-1] != "z":
                    state = 1 
                    stack.pop()
                    # we enter the function to check the final state of the string
                    state = FinalState( InputString, i+1, state, stack)

                break

    # Now we check the state reached at the end of the string
    # if the state is 2, the string is accepted by the PDA, else not.
    if state == 2:
        print("\nThe String is accepted")
    else:
        print("\nThe String is not accepted")


# function to check the next state from state 0 on "0" as input
def NextState(InputString, index, state, stack):

    # we make a copy of the stack for this function and pop out one "0" from its top
    tempStack = stack.copy()
    tempStack.pop()

    # we initialize a temporary state to one
    tempState = 1

    if InputString[index] == "~" and tempStack[-1] == "z":  # "~" indicates "\0"
        tempState = 2

    else:
        # we enter the function to check the final state of the string
        tempState = FinalState( InputString, index + 1, tempState, tempStack)

    if tempState == 2: # if the temporary state is the final state, we return it, else return the actual state
        return tempState
    
    return state


# Function to check the validity of string and go to language validation
def StringValidation():
    # We read a string from the user.
    InputString = input("\nPlease enter the input string having only the characters 0 and 1: ")
    
    # Since python strings do not have "\0" character at the end,
    # a random character "~" is concatenated at the end to 
    # indicate NULL character.
    InputString += "~"      # "~" indicates "\0"

    error = 0 # error variable initialized to check if the string inserted is within given constraints

    # code section to check whether the string is within the constraints 
    i = 0
    while(InputString[i]!="~"):
        if InputString[i]!="0" and InputString[i]!="1":
            print("\nInvalid charecter entered at position", i+1)
            print("\nPlease Try Again WITH A VALID STRING!!!")
            error = 1
            StringValidation()
            break
        i += 1

    if error == 0: # we proceed only if the string inserted is within given constraints
        
        # we enter the function to check if the input string is in the language
        PDA_validation(InputString) 

        # code section to check if the user wants to continue
        print("\nDo you want to check another string?")
        val = input("Press 1 for Yes, and any other key to terminate the program: ")

        if val == "1":
            StringValidation()
        else:
            print("\nProgram Terminated")


# Function to check the final state of the string
def FinalState(InputString, index ,state, stack):

    # we make a copy of the stack for this function
    tempStack = stack.copy()

    while(InputString[index]!="~"): # "~" indicates "\0"
        # we pop out from the stack if head of stack is not "z", else break
        if tempStack[-1] == "z": 
            break
        else: 
            tempStack.pop()
        index += 1

    # we check the top of the stack and whether end of input string, and
    # if it is z, we pop it out and go to the final state
    if InputString[index] == "~" and tempStack[-1] == "z": # "~" = "\0"
        state = 2

    return state


# ============ MAIN PROGRAM ============

# function to check the validity of the string
StringValidation()

