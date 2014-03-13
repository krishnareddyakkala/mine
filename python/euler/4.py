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

"""
is there a better way to do it,other than this seemingly brute force way?
TODO:need to think about a better way of doing this...
"""        
def largest_three_digit_palindrome():
    import itertools
    listing = itertools.product(range(999,500,-1),repeat=2)
    palindrome,tempx,tempy=0,0,0 
    for x,y in listing:
        temp=x*y        
        if(ispalindrome(temp) and temp>palindrome):
             palindrome,tempx,tempy=temp,x,y
    print palindrome,tempx,tempy


if __name__=="__main__":
   largest_three_digit_palindrome()
   
