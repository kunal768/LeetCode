def productExceptSelf(nums):
        n = len(nums)
        curr_left_prod = 1
        left = [1]*n
        for i in range(1,n):
            curr_left_prod = nums[i-1]*curr_left_prod 
            left[i] = curr_left_prod
        print(left)
        curr_right_prod = 1
        for i in range(n-2,-1,-1):
            curr_right_prod = nums[i+1]*curr_right_prod
            left[i] *= curr_right_prod
        print(left)
        # return left


nums = [1,2,3,4]
left = 1
[1,1,2,6]
[24,12,4,1]

productExceptSelf(nums)        
    