from itertools import permutations
if __name__ =="__main__":
   for index,value in enumerate(permutations("0123456789"),start=1):
       if(index==1000000):
          print value
          break

   
