if __name__ =="__main__":
   import math
   globaldict={}
   for num in range(2,10001):
       listt=[1]
       for denom in range(2,int(math.sqrt(num))+1):
           if(num%denom==0):
              listt.append(num/denom)
              listt.append(denom)
       globaldict[num]=sum(listt)
   total=0
   for key,value in globaldict.items():
       if(key !=value and globaldict.get(value,0)==key): 
          total+=key
          print key
   """for key,value in globaldict.items():
       print key ,"and value ",value"""
   
   print total
