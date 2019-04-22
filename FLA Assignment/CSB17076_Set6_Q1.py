# Roll No - CSB17076

# ============ FUNCTIONS ============

def DFAcheck():
    # We read a string from the user.
    InputString = input("\nPlease enter the input string having characters a and b: ")
    
    # Since python strings do not have "\0" character at the end,
    # a random character "~" is concatenated at the end to 
    # take the place of NULL character.
    InputString += "~" 

    # We define three states: 0, 1 & 2
    # State 0 in when 0 b at the end,
    # State 1 in when 1 b at the end, and
    # State 2 in when 2 b at the end. 
    # State 2 is the final state. 
    # The string is accepted if it reaches state 2 at the end.
    state = 0 # start state is 0

    i = 0
    while(InputString[i]!="~"):
        # condition when input is not a or b
        if InputString[i]!="a" and InputString[i]!="b":
            print("\nInvalid charecter entered at position", i+1)
            print("\nPlease Try Again WITH A VALID STRING!!!")
            DFAcheck()
        
        # condition when input is "a"
        # if the state is 0, it remains in 0
        # if the state is 1 or 2, it goes back to 0
        if InputString[i]=="a":
            state = 0

        # condition when input is "b"
        elif InputString[i]=="b":
            # if the state is 0, it goes to 1
            if state == 0:
                state = 1
            # if the state is 1, it goes to 2
            # if the state is 2, it remains in 0
            elif state == 2 or state == 1:
                state = 2

        i += 1

    # Now we check the state reached at the end of the string
    # if the state is 2, the string is accepted by the DFA, else not.
    if state == 2:
        print("\nThe String is accepted")
    else:
        print("\nThe String is not accepted")


    print("""\nDo you want to check another string?
Press 1 for Yes, and any other key to terminate the program""")
    val = input()
    
    if val == "1":
        DFAcheck()
    else:
        print("\nProgram Terminated")


# ============ MAIN PROGRAM ============

# function to check the validity of the string
DFAcheck()

