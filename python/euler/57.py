import sys
from fractions import Fraction
"""
 1+1/2 = 3/2
 1+1/(2+1/2) = 7/5
 1+1/(2+1/(2+1/2)) = 17/12
 so i tried to represent  2+1/2 recurrence as a function!!! 
"""
def Irrational(counter):
    if counter==1:
        return Fraction(1,2)
    return Fraction(1,1)/(Fraction(2,1) + Irrational(counter=counter-1))

if __name__ =="__main__":
   sys.setrecursionlimit(1500)
   number=0
   for counter  in range(1,1001):
       ##we need to add 1 to irrational part.
       fraction = Fraction(1,1)+Irrational(counter)
       if(len(str(fraction.numerator))>len(str(fraction.denominator))):
           number=number+1
   print number 
    


