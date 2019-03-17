#Modify the constructor for the fraction class so that it checks to make sure that the numerator and denominator are both integers. If either is not an integer the constructor should raise an exception.


def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Please input an integer!")
       continue
    else:
       return userInput 
       break

n = int(inputNumber("input numerator"))
d = int(inputNumber("input denominator"))

class Fraction:
  def __init__(self,top,bottom):

    self.num = top
    self.den = bottom

  def __str__(self):
    return str(self.num) + "/" + str(self.den)

  def getNum(self):
    return self.num

  def getDen(self):
    return self.den

myfraction = Fraction(n,d)

print(myfraction)