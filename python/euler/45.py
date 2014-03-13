"""
Another way to solve without storing the results in lists is , compute the nth triangle number 

and  find the roots of the below quadratic equations 

3i^2-i-2x=0
2i^2-i-x=0
 where x is computed from i*(i+1)/2 ..

If we can find the integer roots for both of these equations,then we can say that  triangle
number x is also pentagonal and hexagonal.

"""

if __name__ =="__main__":
   triangle=[]
   pentagonal=[]
   hexagonal=[]
   i=1
   while True:
         t=(i*(i+1))/2
         triangle.append(t)
	 pentagonal.append((i*(3*i-1))/2)
	 hexagonal.append(i*(2*i-1))
         if((t in pentagonal) and (t in hexagonal)):
             print t
             if (t!=1 and t!=40755):
                 break
         i=i+1

          
  
