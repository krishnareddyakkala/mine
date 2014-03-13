def gen_triangle():
    start=1
    while True:          
          yield (start*(start+1))/2
	  start=start+1



if __name__ =="__main__":
   listt=[]
   for i in open('words.txt'):
       listt.extend(i.split(','))
   listt.sort()
   lookup={}
   for i  in listt:
       temp=0
       for j in i:
           if(ord(j) not in(34,39)):
              temp+=(ord(j)-64)
       lookup[str(i)]=temp
   maximum = max(list(lookup.values()))
   temporary=[]
   for i in gen_triangle():
       if i<=maximum:
          temporary.append(i)
       else:
           break
   print sum([ 1 for  i in lookup.values() if i in temporary])
 
   

