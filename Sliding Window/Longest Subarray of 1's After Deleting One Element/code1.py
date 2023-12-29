class Solution:
    def longestSubarray(self, nums):
        left=right=0    
        k = 1
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            
        return right-left
        
nums = [0,1,1,0,1,1,1,0,0,1,1,0,0,0,0,0,1,1,1,0,0,0]
nums1 = [1,0,1,1,1,1,0,0,1,1,1,0,1,1,1,0,1,1,0,0,1]
nums2 = [0,1,1,1,0,1,1,0,1]
# nums3 = [1,1,1,0]
obj = Solution()
print(obj.longestSubarray(nums)) 