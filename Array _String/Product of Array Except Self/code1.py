import math
class Solution:
    def productExceptSelf(self, nums):
        length = len(nums)
        products = [1] * length
        for i in range(1, length):
            products[i] = products[i-1] * nums[i-1]

        right = nums[-1]
        for i in range(length-2, -1, -1):
            products[i] *= right
            right *= nums[i]
        
        return products


nums = [1,2,3,4]
nums2 = [-1,1,0,-3,3]
obj = Solution()
print(obj.productExceptSelf(nums))