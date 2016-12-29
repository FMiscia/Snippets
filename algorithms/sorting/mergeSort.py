#The idea is to merge 2 sorted array, 
#until we sort the entire array
def merge(A,start,mid,end):
	p = start
	q = mid+1
	T = []
	for i in range(0,end+1):
		T.append(A[i])
	current = start
	while (p <= mid and q <= end):
		if (T[p] < T[q]):
			A[current] = T[p]
			p=p+1
		else:
			A[current] = T[q]
			q=q+1
		current = current + 1

	if(p<=mid):
		for i in range(p,mid+1):
			A[current] = T[i]
			current = current + 1
	elif (q<=end):
		for i in range(q,end+1):
			A[current] = T[i]
			current = current + 1
	

def mergeSort(A,start,end):
	if(start<end):
		mid = (start+end)/2
		mergeSort(A,start,mid)
		mergeSort(A,mid+1,end)
		merge(A,start,mid,end)

A = [11,4,2,1,3,0,9]
l = len(A)
mergeSort(A,0,l-1)
print str(A)
