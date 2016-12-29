#Exexutes the XOR of each subarray of the given array
#Since each element appears (N-i)(i+1) times, only the elements that appear an odd number of times are XORed
#If N is even so the result is always 0, since every number appears an even number of times
#If N is odd, only even index the number that appears an odd number of times, so the result is the XOR betwen even index number
def subarray_xor(N,A):
	result = 0
	if N%2==0:
		return 0
	for i in xrange(0,N,2):
		result = result ^ A[i]
	return result

A = [3,5,1]
N =  3
print str(subarray_xor(N,A))