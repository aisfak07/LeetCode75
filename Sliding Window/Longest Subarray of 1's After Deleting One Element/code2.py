class Solution:
    def longestSubarray(self, nums):
        countZero = ans = 0
        right = left = 0
        if 0 not in nums or nums.count(0)<2:
            return len(nums)-1
        elif 1 not in nums:
            return 0
        else:
            for right in range(len(nums)):
                if nums[right] == 0:
                    countZero += 1

                while countZero > 1:
                    if nums[left] == 0:
                        countZero -= 1
                    left += 1

                ans = max(ans, right - left + 1 - countZero)
            
                    
                
        return ans

nums = [0,1,1,1,0,1,1,0,1]
# nums3 = [1,1,1,0]
obj = Solution()
print(obj.longestSubarray(nums)) 