"""
@ Kunal KS Sahni 
@ IP = [1,2,3,4]
@ OP = [2,4,4,4]

""" 


def decompressRLElist(nums):
	result = []
	n = len(nums)
	for i in range((n-1)//2 + 1):
		result += (nums[2*i]*[nums[2*i+1]])
	# print([2]*3)
	print(result)


decompressRLElist([1,1,2,3])

# print()





