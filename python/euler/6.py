"""
1+2+3.......n=n(n+1)/2
1^2+2^2+3^2.......n^2=n(n+1)(2n+1)/6
"""
def diff_squaresofsum_and_sumofsquares(n):
    sumofsquares = (n*(n+1)*(2*n+1))/6
    sumofnum = (n*(n+1))/2
    squaresofsum = sumofnum*sumofnum
    return  squaresofsum- sumofsquares

if __name__=="__main__":
   print diff_squaresofsum_and_sumofsquares(100)

