"""
the triangle number sequence is .. 1 3  6 10 15 21
"""
def gen_triangle_num():
    yield 1
    summation=1
    i=2
    while True:
        summation,i=summation+i,(i+1)       
        yield summation

"""
this is actually n*(n+1)/2
"""
def gen_triangle_seq():
    start=1
    while True:
          yield start*(start+1)/2
          start=start+1
         
 

if __name__ =="__main__":
   import math
   globaldict={}
   for num  in gen_triangle_seq():
       listt=[1]
       for denom in range(2,int(math.sqrt(num))+1): 	 	
           if(num%denom==0):
              listt.append(num/denom)
              listt.append(denom) 	 	
       #globaldict[num]=len(listt)
       if(len(listt)>=500):
           print num
           break

 	 	
   
