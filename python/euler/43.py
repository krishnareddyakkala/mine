from itertools  import permutations

if __name__ =="__main__":
   summation=0
   for i in permutations("0123456789"):
       i="".join([j for j in i])
       if(int(i[1:4])%2==0 and int(i[2:5])%3==0 and \
          int(i[3:6])%5==0 and int(i[4:7])%7==0 and \
          int(i[5:8])%11==0 and int(i[6:9])%13 ==0 and \
          int(i[7:10])%17 ==0):
          summation=summation+int(i)
   print summation
    
          
       
