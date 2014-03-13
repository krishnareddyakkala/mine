import math

"""
function to generate infinite prime numbers!!!
"""
def gen_prime():
    yield 2
    x=3
    while True:
        if x>1000000:
           break
        elif(is_prime(x) and should_not(x)):
            yield x
        x=x+2

def is_prime(x):
    if x==1:
       return False
    for i in range(3,int(math.sqrt(x))+1,2):
        if(x%i==0):
            return False
    return True
"""
the idea is -if it cotains any even number ,then it will not be a prime after rotations..
and remove zero as it's presence will make 103 as 31 and 13 then we will loss one number in the digit.
"""

def should_not(n):
    cache =str(n)
    return (not "0" in cache) and (not "2" in cache) and (not "4" in cache) and (not "6" in cache) and (not "8" in cache)

if __name__ =="__main__":
   total=0
   for i in gen_prime():
       flag=True
       original=i
       if len(str(i))==1:
          total=total+1
       else:
           for j in range(len(str(i))):
                 if(not is_prime(i)):
                    flag=False
                 i=int(str(i)[1:]+str(i)[:1])
           if flag:
              total=total+1
   print total 
           
