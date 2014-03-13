
def gen_sequence():
   start=1
   yield start
   threshold = 3
   add=2
   end = 1001*1001
   while start<end:
         if(start<(threshold*threshold)):
            start=start+add            
         else:
             add=add+2
             start=start+add
             threshold=threshold+2
         yield start

if __name__ =="__main__":
   print sum([i for i in gen_sequence()])   
