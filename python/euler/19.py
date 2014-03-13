from datetime import  date


"""
I should also try to solve the other way,as day of week (sunday,monday....etc) 
is handled by datetime...

Have to think and write considering leap year and blah ,blah.....
python handles days of week as follows:
monday --0
.......
.......
saturday --5
sunday --6
"""
if __name__ =="__main__":
   total=0
   for year in range(1901,2001):
       for month in range(1,13):
           d=date(year,month,1)
           if(d.weekday()==6):
              total=total+1
   print total

