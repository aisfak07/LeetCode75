class Solution:
    def findMaxAverage(self, nums, k) -> float:
        current_sum = 0
        x = k
        i = 0
        max_sum = current_sum = sum(nums[i:k])

        
        if x == len(nums):
            max_sum = sum(nums)
        elif x == 1:
            max_sum = max(nums)
        elif x > 1:
            while i <= len(nums)-x-1:
                current_sum = current_sum + nums[k] - nums[i]
                if max_sum < current_sum:
                    max_sum = current_sum
                i += 1
                k+=1
        
        return max_sum/x



nums = [9,7,3,5,6,2,0,8,1,9]


k = 6
obj = Solution()
print(obj.findMaxAverage(nums, k))
# accepted 