class Solution:
    def longestOnes(self, nums, k):
        n = len(nums)
        count = 0
        for i in nums:
            if i == 0:
                count += 1
        return n-(count-k)

nums = [0,1,1,1,0,1,1,0,1]
k = 2
obj = Solution()
print(obj.longestOnes(nums, k))