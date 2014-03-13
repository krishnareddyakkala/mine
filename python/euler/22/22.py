if __name__ =="__main__":
   listt=[]
   for i in open('names.txt'):
       listt.extend(i.split(','))
   listt.sort()
   summing=0
   for counter,i  in enumerate(listt,start=1):
       temp=0
       for j in i:
           if(ord(j) not in(34,39)):
              temp+=(ord(j)-64)
       summing+=counter*temp
   print summing
              
