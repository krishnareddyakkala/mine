
"""
problem #2
""" 
def gen_fibo(upper):
    i,j=1,2
    while i<upper:        
        yield i
        i,j=j,(i+j)
       
def fibo_sum():
    return sum(filter(lambda a: a%2==0, gen_fibo(4000000)))

if __name__=="__main__":
   print fibo_sum()
