class Solution:
    def longestSubarray(self, nums):
        nums.remove(nums[2])
        print(nums)

nums = [0,1,1,0,0,1,1]
obj = Solution()
print(obj.longestSubarray(nums)) 