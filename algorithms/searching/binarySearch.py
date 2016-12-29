def findXBinarySearch(min,max,x):
	mid = min+max >> 1
	if(x<elements[mid]):
		if(reverse):
			return findXBinarySearch(mid+1,max,x)
		return findXBinarySearch(min,mid-1,x)
	if(x>elements[mid]):
		if(reverse):
			return findXBinarySearch(min,mid-1,x)
		return findXBinarySearch(mid+1,max,x)
	else:
		if(reverse):
			return lenght-mid
		else:
			return mid+1

inputs = []
values = raw_input()	
lenght = int(values)
values = raw_input()
elements = [int(val) for val in values.split(" ")]
num_inputs = int(raw_input())
inputs = []
for i in range(num_inputs):
	inputs.append(int(raw_input()))
for i in range(num_inputs):
	print str(findXBinarySearch(0,lenght-1,inputs[i]))