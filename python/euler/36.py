"""
A function to check whether a number is a palindrome or not!!!
"""
def ispalindrome(num):
    resultnum=0
    temp = num
    while num !=0:
        x,y = divmod(num,10)
        resultnum=resultnum*10+y
        num=x
    return temp == resultnum


if __name__ =="__main__":
   print sum([i for i in range(1,1000000) if ispalindrome(i) and ispalindrome(int(str(bin(i))[2:]))])
    
