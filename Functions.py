#Takes a list called "thelist" containing all numbers.
#Returns the product of those numbers.

def product (thelist):
    product = 1
    for n in thelist:
        product *= n
    return product
    
#Increments all numbers in "thelist" by "inc".  "inc" is a number.

def increment_list (thelist, inc):
    for i in range (len(thelist)):
        thelist[i] += inc


#This function takes 3 parameters a, b, c which are all numbers.  The function returns the largest value of the 3 parameters.  For example, calling
#largest (19, 17, 19) would return 19 and the calling largest (513, 600, 54) would return 600.

def largest (a, b, c):
    if (a >= b) and (a >= c):
        return a
    elif b >= c:
        return b
    else:
        return c

def main():
    ###############################################
    print("\nTest 1 -- product")
    if product([3, 2, 4]) == 24:
        print("Test 1.1 - passed")
    else:
        print("Test 1.1 - failed")

    if product([10, 2, 3, 5]) == 300:
        print("Test 1.2 - passed")
    else:
        print("Test 1.2 - failed")


    ###############################################
    print("\nTest 2 -- increment_list")
    list1 = [15, 2, 45]
    increment_list(list1, -2)
    if str(list1) == "[13, 0, 43]":
        print("Test 2 - passed")
    else:
        print("Test 2 - failed")

    ###############################################
    print("\nTest 3 -- largest")
    if largest(9, 2, 7) == 9:
        print("Test 3.1 - passed")
    else:
        print("Test 3.1 - failed")

    if largest(12, 12, 8) == 12:
        print("Test 3.2 - passed")
    else:
        print("Test 3.2 - failed")

    if largest(5, 12, 84) == 84:
        print("Test 3.3 - passed")
    else:
        print("Test 3.3 - failed")


main()
