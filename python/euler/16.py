def sum_of_digits_in_two_power_onethousand():
    """
    start with 2^0 (i.e. 1),then iterate the process for 1000 times.
    2^n = 2^n-1 + 2^n-1
    """
    summation=1
    for i in range(0,1000):        
        summation = summing(str(summation),str(summation))         
    return sum([int(j) for j in summation])    
        

def summing(one,two):    
    if(len(one)<len(two)):        
        one=one.rjust(len(two),'0')        
    elif(len(one)>len(two)):        
        two=two.rjust(len(one),'0')    
    temp=0
    result=""
    for i,j in zip(one[::-1],two[::-1]):
        temp=temp+int(i)+int(j)
        result=result+str(temp%10)
        temp=temp/10
    temp=str(temp)[::-1]    
    result=result+temp
    result=result[::-1]
    if(result.startswith('0')):
        return result[1:]
    return result

if __name__ =="__main__":
   print sum_of_digits_in_two_power_onethousand()
