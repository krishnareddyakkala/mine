from decimal import Decimal
from fractions import Fraction
from operator import mul

if __name__ =="__main__":
   listt=[]
   for denom in range(10,100):
       for num in range(10,denom):
               if(str(num)[1]==str(denom)[0]):                 
 		  xnum=int(str(num)[0])
		  xdenom=int(str(denom)[1])
                  if(xdenom!=0 and Fraction(num,denom)==Fraction(xnum,xdenom)):
                      listt.append(Fraction(num,denom))
   print reduce(mul,(i for i in listt)).denominator

                      
      
                  


                     
       
