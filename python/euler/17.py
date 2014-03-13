def calculate_no_of_words():
    holder = buildholder()
    count=0
    for i in range(1,1001):
	key=str(i)
	if(holder.has_key(key)):
	     count+=len(holder[key])
             print holder[key]
        elif(len(key)==2):
	     key1,key2 =str(key[:1])+"0",str(key[1:])
             count+=len(holder[key1])
	     count+=len(holder[key2])
             print holder[key1],holder[key2]
        else:
             if(i%100==0):
                 count+=len(holder[key[:1]]+"hundred")
		 print holder[key[:1]]+" hundred"
	     else:
                 key1,key2 =str(key[:1]),str(key[1:])    
		 count+=len(holder[key1]+"hundredand")
	     	 if(holder.has_key(key2)):
                    count+=len(holder[key2])
                    print holder[key1]+" hundred and ",holder[key2]
                 else:
                    key3,key4 =str(key2[:1])+"0",str(key2[1:])
             	    count+=len(holder[key3])
                    count+=len(holder[key4])
                    print holder[key1]+" hundred and ",holder[key3],holder[key4]

    return count
  	             
def buildholder():
     holder={}
     holder["1"]= holder["01"]="one"
     holder["2"]= holder["02"]="two"
     holder["3"]= holder["03"]="three"
     holder["4"]= holder["04"]="four"
     holder["5"]= holder["05"]="five"
     holder["6"]= holder["06"]="six"
     holder["7"]= holder["07"]="seven"
     holder["8"]= holder["08"]="eight"
     holder["9"]= holder["09"]="nine"
     holder["10"]="ten"
     holder["11"]="eleven"
     holder["12"]="twelve"
     holder["13"]="thirteen"
     holder["14"]="fourteen"
     holder["15"]="fifteen"
     holder["16"]="sixteen"
     holder["17"]="seventeen"
     holder["18"]="eighteen"
     holder["19"]="nineteen"
     holder["20"]="twenty"
     holder["30"]="thirty"
     holder["40"]="forty"
     holder["50"]="fifty"
     holder["60"]="sixty"
     holder["70"]="seventy"
     holder["80"]="eighty"
     holder["90"]="ninety"
     holder["1000"]="onethousand"
     return holder


if __name__=="__main__":
   print  calculate_no_of_words()
