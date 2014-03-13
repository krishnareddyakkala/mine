
"""
euler problem -14
"""

def longest_sequence(n,count):
    if(n==1):
        return count+1
    if(n%2==0):
        return longest_sequence(n/2,count=count+1)
    else:
        return longest_sequence(3*n+1,count=count+1)
        
def collatz_conjecture():
    max=0
    num=0
    dict={}
    for i in range(1000000,0,-1):
        temp=longest_sequence(i, 0)
        if(temp>max):
            max=temp
            num=i 
        dict[i]=temp       
    return  max,num


if __name__=="__main__":
   print collatz_conjecture()
    #print longest_sequence(13,0)
