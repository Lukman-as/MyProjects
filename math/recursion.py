def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Base case: If exp is 0, the result is always 1.
    if exp == 0:
        return 1
    # Recursive case: Calculate base^exp by multiplying base with base^(exp-1).
    else:
        return base * iterPower(base, exp - 1)

def main():
    x = input("Enter base:")
    y = input("Enter exponential:")
    a = iterPower(int(x), int(y))
    print(a)

if __name__ == "__main__":
    main()
