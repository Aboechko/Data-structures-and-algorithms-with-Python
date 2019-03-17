#Modify the constructor for the Fraction class so that GCD is used to reduce fractions immediately. Notice that this means the __add__ function no longer needs to reduce. Make the necessary modifications.
def gcd(m,n):
  while m%n != 0:
    oldm = m
    oldn = n

    m = oldn
    n = oldm%oldn

    return n
    
class Fraction:
  def __init__(self,top,bottom):

    self.num = top
    self.den = bottom

  def __str__(self):
    return str(self.num) + "/" + str(self.den)

  def simplify(self):
    common = gcd(self.num, self.den)

    self.num = self.num // common
    self.den = self.den // common
