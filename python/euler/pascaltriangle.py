def pascal_triangle(n):
    temp=[]
    counter=0
    while counter<=n:
          k=0
          another=[]
          for i in temp:
              another.append(i+k)
              k=i
          another.append(1)
          temp=another
          counter=counter+1
          yield another

##usage of pascal triangle..
def main():
    for i in pascal_triangle(7):
        print i

if  __name__=="__main__":
    print "I am printing a pascal triangle upto 7th power"
    main()

"""
For n you will get n+1 rows because 0'th power is also included in the series. 
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]
[1, 6, 15, 20, 15, 6, 1]
[1, 7, 21, 35, 35, 21, 7, 1]
"""
