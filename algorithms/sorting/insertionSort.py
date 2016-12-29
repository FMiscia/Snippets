#Each element greater that the current element is shifted forward
def insertionSort(length,elements):
	for i in range(0,length):
		temp = elements[i]
		j = i
		#if the prev element is greater than temp, then is shifted forward
		#and j is decremented
		while(j > 0 and elements[j-1] > temp):
			elements[j] = elements[j-1]
			j = j-1
		elements[j] = temp
	return elements

def findXBinarySearch(min,max,x):
	mid = min+max >> 1
	if(x<result[mid]):
		if(reverse):
			return findXBinarySearch(mid+1,max,x)
		return findXBinarySearch(min,mid-1,x)
	if(x>result[mid]):
		if(reverse):
			return findXBinarySearch(min,mid-1,x)
		return findXBinarySearch(mid+1,max,x)
	else:
		if(reverse):
			return lenght-mid
		else:
			return mid+1



length = int(raw_input())	
values = raw_input()
elements = [int(val) for val in values.split(" ")]
unordered = elements[:]
result = insertionSort(length,elements)
print result
reverse = result[0] > result[1]
for val in unordered:
	print str(findXBinarySearch(0,length,val)),
