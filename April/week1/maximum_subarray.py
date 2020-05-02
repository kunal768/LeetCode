# kadane baby
import sys  
def maxSubArray(arr):
	curr_maxx = -sys.maxsize - 1
	maxx = curr_maxx
	n = len(arr)
	for i in range(n) :
		curr_maxx = max(arr[i],arr[i]+curr_maxx)
		maxx = max(maxx,curr_maxx)
	return maxx


