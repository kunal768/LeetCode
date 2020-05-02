def findNonzero(arr,i,n):
    for j in range(i+1,n):
        if arr[j] != 0 :
            return j
    return -1

def moveZeroes(nums):
    n = len(nums)
    for i in range(n):
        if(nums[i] == 0):
            j = findNonzero(nums,i,n)
            nums[i],nums[j] = nums[j],nums[i]
            
    return nums

print(moveZeroes([12,1,3,0,0,4,5]))