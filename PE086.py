def isInt(a,b):
    squared = a*a + b*b
    if int(squared**0.5)**2 == squared:
        return True
    return False

# The total number for M=100 is 2060, given in the problem.
# I don't calculate for each value of M; I only calculate
# the number of new combinations where one of the sides is
# *exactly* M, since the total already includes all possibilities
# for shorter sides.
M = 100
total = 2060
while total <= 1000000:
    M += 1
    # If the two shorter sides add up to less than
    # the longest side, there are i//2 pairs of values
    for i in range(1, M+1):
        if isInt(M, i):
            total += i//2
    # If the two shorter sides add up to more
    # than the longest side, but not more than double,
    # since M is the maximum, there are this number
    # of pairs of values where neither one is greater
    # than the longest side:
    for i in range(M+1, M*2+1):
        if isInt(M, i):
            total += (M+M-i)//2 + 1
            # e.g., if M is 10 and the other two sides add up to 15,
            # they could be (5,10), (6,9), or (7,8):
            #10 .. 15 = 3
            #10 .. 16 = 3
            #10 .. 17 = 2
            #10 .. 18 = 2
            #10 .. 19 = 1
            #10 .. 20 = 1

print(M)
        
