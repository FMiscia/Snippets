def findX(x,elements):
	counter=1
	for val in elements:
		if val == x:
			pos = counter
		counter = counter + 1  
	return pos
	
x = 1
elements = [1,2,3,4,1] 
print str(findX(x,elements))