import math

"""
function to generate infinite prime numbers!!!
"""
def gen_prime():
    yield 2
    x=3
    while True:
        if(is_prime(x)):
            yield x
        x=x+2

def is_prime(x):
    for i in range(3,int(math.sqrt(x))+1,2):
        if(x%i==0):
            return False
    return True

def largest_primefactor():
    cache=int(math.sqrt(600851475143))
    temp=None
    for i in gen_prime():
        if(i<=cache and 600851475143%i==0):
           temp=i
        elif(i>cache):
            break
    return temp

if __name__=="__main__":
   print largest_primefactor()


