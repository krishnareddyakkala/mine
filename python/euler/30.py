"""
dirty double evaluation of sum([j**5 for j in map(int,str(i))]) ,but who cares ? :)
"""
if __name__ == "__main__":
   print sum( [sum([j**5 for j in map(int,str(i))]) for i in range(10,1000000) if sum([j**5 for j in map(int,str(i))])==i ])
        
