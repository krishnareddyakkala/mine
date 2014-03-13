"""
A function to check whether a number is a palindrome or not!!!
"""
def is_palindrome(num):
    resultnum=0
    temp = num
    while num !=0:
        x,y = divmod(num,10)
        resultnum=resultnum*10+y
        num=x
    return temp == resultnum

def is_lycheral(n,count=50):
    temp = n+int(str(n)[::-1])
    print n
    if(count==0):
	return True
    if(is_palindrome(temp)):
       return False
    else:
       return is_lycheral(temp,count=count-1)
    


if __name__ =="__main__":
   """for i in range(1,10000):
       if is_lycheral(i):
          print i"""
   print sum([1 for i in range(1,10000) if is_lycheral(i)])
       
