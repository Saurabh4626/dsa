class Fraction:
    def __init__(self,num=0,den=1): ##it sets default attributes value if value isn't provided
        self.num=num
        self.den=den
    def print(self):
        print(self.num,'/',self.den)
f=Fraction()
f1=Fraction(2,3)
f1.print()