try:
    n = int(input("enter numerator"))
    d = int(input("enter denominator"))
    print(n / d)
except ZeroDivisionError:
    print(" denominator should be greater than 1")