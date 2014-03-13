array=[[0,2,0,0,4,0,0,5,0],[0,0,0,7,2,6,0,0,0],[0,0,7,0,9,0,6,0,0],
[7,0,8,0,5,0,2,0,6],[9,0,0,0,0,0,0,0,4],[5,0,1,0,8,0,7,0,9],
[0,0,6,0,1,0,8,0,0],[0,0,0,8,7,3,0,0,0],[0,7,0,0,6,0,0,4,0]]

def find(llist,value):
    return value in llist

def sudoku():
    while(0 in [array[i][j] for i in range(9) for j in range(9)]):
          for i in range(1,10):
	      for j in range(9):
                  count=0;
                  for k in range(9):
                      if(array[j][k] ==0):
			  a=[array[j][l] for l in range(9)];
			  b=[array[l][k] for l in range(9)];
			  c=[array[l][m] for l in range((j-j%3),(j-j%3)+3) for m in range((k-k%3),(k-k%3)+3) ];
			  if(not find(a,i) and not find(b,i) and not find(c,i)):
				count,row,column=count+1,j,k;
		  if(count==1):
		     array[row][column]=i;

if __name__ == "__main__":
   sudoku()
   for element in array:
       print element;


