def PEisPrime(inp):
    if inp < 2:
        return False
    elif inp == 2:
        return True
    else:
        fact = 3
        while fact < inp**0.5+2:
            if not inp % fact:
                return False
        return True

    
