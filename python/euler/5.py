"""
The lcm and gcd functions 
"""
def lcm(a,b):
    return a*b/gcd(a,b)

def gcd(a,b):
    while b>0:
        a,b =b,a%b
    return a


"""
smallest divisor for numbers between 1 ,2,3,.....20 is 
their LCM.
"""
def min_divisor():
    x=1
    for i in range(1,21):
        x=lcm(x,i)
    print x

if __name__=="__main__":
   min_divisor()
