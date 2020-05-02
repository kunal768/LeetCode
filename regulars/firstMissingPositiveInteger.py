# # interview bit 
# from collections import OrderedDict
# forarr.sort()
# [-8,-7,-6]

def firstMissingPositive(arr):
	arr.sort()
	hashmap = set(arr)
	for i in range(arr[0],arr[-1]+1):
		if i+1 > 0 and (i+1 not in hashmap) :
			return i+1
	return 1


arr = [-8,-7,-6]
print(firstMissingPositive(arr))
