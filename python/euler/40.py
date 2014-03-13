def pump_out():
    n=1
    while True:
          for i in map(int,str(n)):
              yield i
          n=n+1



if __name__=="__main__":
   product=1
   for index,value in enumerate(pump_out(),start=1):
       if(index>1000000):
           break
       if (index==1 or index==10 or \
           index==100 or index==1000 or \
           index==10000 or index==100000 or \
           index==1000000):
           product=product*value
   print product



    
