def findX(x,elements,lenght):
	for index in xrange(lenght-1,0,-1):
		if elements[index] == x:
			return index+1

values = raw_input("Write the array size and the number you are looking for: ")	
lenght,x = (int(val) for val in values.split(" "))
values = raw_input("Write the array: ")
elements = [int(val) for val in values.split(" ")]
print str(findX(x,elements,lenght))
