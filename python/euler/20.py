"""
since python supports large integers ,this was solved easily.
"""

if __name__=="__main__":
   i=1
   for j in range(1,101):
       i=i*j
   print sum(map(int,str(i)))

   
