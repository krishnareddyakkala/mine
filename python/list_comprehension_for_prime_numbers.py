'''
python list comprehension to print primary numbers
'''
print [x for x in range(2,50) if not [y for y in range(2,x) if x%y ==0]]
