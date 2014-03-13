import math

def gen_prime():
    x=11  #start with 11 as 2 5 7 are not truncatable primes. 
    while True:
        if(is_prime(x)):
            yield x
        x=x+2

def pump_out(n):
    temp=n
    while n>0:
          yield n
          n=n/10
    n=str(temp)
    i=0
    while i<len(n):
          yield int(n[i:])
          i=i+1
          
          

def are_all_primes(n):
    for i in pump_out(n):
         if not is_prime(i):
            return False
    return True


def is_prime(x):
    if x==1:
       return False
    count=0
    for i in range(1,int(math.sqrt(x))+1):
        if(x%i==0):
            count=count+1
    if(count>1):
        return False
    return True

if __name__ =="__main__":
   listt=[]
   for i in gen_prime():
       if are_all_primes(i):
          listt.append(i)
       if len(listt)==11:
          break
   print listt
   print sum(listt)


        
       
  
