class Solution:
    def pivotIndex(self, nums):
        totalsum = sum(nums)
        for pivot in range(len(nums)):
            subOne = sum(nums[:pivot])
            subTwo = sum(nums[pivot+1:])

            if subOne == subTwo:
                return pivot
            
        return -1

nums = [1,7,3,6,5,6]
obj = Solution()
print(obj.pivotIndex(nums)) 