## custom exception

class BASIC_MATHS_SIKH_KR_AA(Exception):
    pass
try:
    n = int(input("enter numerator"))
    d = int(input("enter denominator"))
    if d==0:
        raise BASIC_MATHS_SIKH_KR_AA()
    print(n / d)
except BASIC_MATHS_SIKH_KR_AA:
    print("Basic Maths Sikh Le")