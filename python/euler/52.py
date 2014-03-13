def is_same(n,m):
    lista= sorted(map(int,str(n)))
    listb= sorted(map(int,str(m)))
    return lista==listb  
    

if __name__ =="__main__":
   start=1
   while True:
         if (is_same(start,2*start) and is_same(start,3*start) \
             and is_same(start,4*start) and is_same(start,5*start) \
             and is_same(start,6*start)):
             break
         else:
             start=start+1

   print start
