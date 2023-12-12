class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in nums:
            if i != 0:
                nums[count] = i
                count += 1
        
        while(count < len(nums)):
            nums[count] = 0
            count += 1
        
        
nums = [0,1,0,3,12]
obj = Solution()
obj.moveZeroes(nums)
        