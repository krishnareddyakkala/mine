import math

def gen_prime():
    yield 2,1
    count=2
    x=3
    while True:
        if(no_of_multipliers(x)):
            yield x,count
            count=count+1
        x=x+2

def ten_thousand_one_prime():
    for i,nth in gen_prime():
        if(nth==10001):
          return i

def no_of_multipliers(x):
    count=0
    for i in range(1,int(math.sqrt(x))+1,2):
        if(x%i==0):
            count=count+1
    if(count>1):
        return False
    return True


if __name__=="__main__":   
   print ten_thousand_one_prime(),"is 10,001th prime number"
