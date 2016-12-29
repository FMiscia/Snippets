def bubbleSortSwappingNumber(length,elements):
	numberOfSwap = 0
	for i in range(0,length-1):
		for j in range(0,length-i-1):
			if(elements[j] > elements[j+1]):
				numberOfSwap = numberOfSwap + 1
				temp = elements[j]
				elements[j] = elements[j+1]
				elements[j+1] = temp
	return numberOfSwap

values = raw_input()	
length = int(values)
values = raw_input()
elements = [int(val) for val in values.split(" ")]
print (str(bubbleSortSwappingNumber(length,elements)))