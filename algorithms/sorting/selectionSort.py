#We try always to find the index of the minimum element
def selectionSort(length,x,elements):
	minimum = 0
	for i in range(0,length):
		minimum = i;
		#if(i == x):
		#	return elements
		for j in range(i+1,length):
			if(elements[minimum] > elements[j]):
				minimum = j
		#once the minimum is found we swap the elements
		swap(i,minimum,elements)
	return elements


def swap(x1,x2,elements):
	temp = elements[x1]
	elements[x1] = elements[x2]
	elements[x2] = temp
	

values = raw_input()	
length,x = (int(val) for val in values.split(" "))
values = raw_input()
elements = [int(val) for val in values.split(" ")]
result = selectionSort(length,x,elements) 
print ' '.join(str(val) for val in result)