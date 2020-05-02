
# better approach 
def smallerNumbersThanCurrent(nums):
	n = len(nums)
	temp = nums
	nums = sorted(nums)
	d = {}
	for i in nums :
		d[i] = nums.index(i)
	result = [d[i] for i in temp]
	print(result)
	return result



# chutiya approaach = two pointer 
def smallerNumbersThanCurrent(nums):
	# print(nums)
	n = len(nums)
	
	temp = nums 

	nums = sorted(nums,reverse = True)

	d = {}

	for head in range(n):
		count = 0
		arr = []
		for tail in range(n-1,head,-1):
			if nums[tail] < nums[head] :
				# print(nums[tail])
				arr.append(nums[tail])
				count += 1
		d[nums[head]] = count 


	result = []

	for i in range(n):s
		result.append(d[temp[i]])

	print(result)
	return result



smallerNumbersThanCurrent([8,1,2,2,3])