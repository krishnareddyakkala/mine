if __name__ =="__main__":
   print max([sum(map(int,str(i**j))) for i in range(1,100) for j in range(1,100)])

