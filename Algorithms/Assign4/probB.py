def CountBall( n ):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return ( n**2 + CountBall(n-1) )
    
level = int(input('Enter the level:'))

print("Total no. of balls:",CountBall( level ),"\nNo. of balls in that level:", level**2)

