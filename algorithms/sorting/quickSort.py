#Swap all the elements smaller then pivot on its left
# and greater elements on its right
def partition(A,start,end):
	piv = A[start]
	i = start+1
	# i is incremented only if there is a swap. It defines the region of smaller elements
	for j in range(start+1,end+1):
		if(piv > A[j]):
			swap(i, j, A)
			i = i+1
	#At the end the pivot is swapped with the last element smaller than itself
	swap(start,i-1,A)
	return i-1
	
def swap(a,b,A):
	temp = A[a]
	A[a] = A[b]
	A[b] = temp
	
def quickSort(A,start,end):
	if(start < end):
		piv = partition(A,start,end)
		quickSort(A,start,piv-1)
		quickSort(A,piv+1,end)
	return A

values = raw_input()	
length = int(values)
values = raw_input()
A = []
A = [int(val) for val in values.split(" ")]
result = quickSort(A,0,length-1)
print ' '.join(str(val) for val in result)
