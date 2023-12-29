class Solution:
    def longestSubarray(self, nums):
        l=r=0    
        k = 1
        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
            
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
            
        return r-l

nums = [0,1,1,1,0,1,1,0,1]
# nums3 = [1,1,1,0]
obj = Solution()
print(obj.longestSubarray(nums)) 