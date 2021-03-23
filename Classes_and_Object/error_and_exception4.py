##else and finally
try:
    n = int(input("enter numerator"))
    d = int(input("enter denominator"))
    c=n/d
except ZeroDivisionError:
    print(" denominator should be greater than 1")
except ValueError:
    print("Enter integer value")
else:
    ##if no exception has been raised this
    ## this block of code will be executed
    print(c)
finally:
    print(n)
    print(d)
    print("exception may or may not be raised")
