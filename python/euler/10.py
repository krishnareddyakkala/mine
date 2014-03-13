import math

def gen_prime():
    yield 2
    x=3
    while True:
        if(no_of_multipliers(x)):
            yield x
        x=x+2


def no_of_multipliers(x):
    count=0
    for i in range(1,int(math.sqrt(x))+1,2):
        if(x%i==0):
            count=count+1
    if(count>1):
        return False
    return True

def sum_of_primes_below_2million():
    summation=0
    for i in gen_prime():
        if(i<2000000):
            summation+=i
        else:
            break
    return summation

if __name__=="__main__":
#   print "sum of primes below 2 million is :",sum_of_primes_below_2million()
    print sum_of_primes_below_2million()
