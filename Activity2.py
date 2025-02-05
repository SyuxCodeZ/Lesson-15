for x in range(30):
    if (x % 15) == 0:
        pass
    elif (x % 20) == 0:
        print ("fizz")
    elif (x % 5) == 0:
        print ("buzz")
    elif (x % 3) == 0:
        print ("yes")
    else:
        print (x)