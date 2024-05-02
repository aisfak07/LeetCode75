class Solution:
    def findMaxAverage(self, nums, k):
        total = sum(nums[:k])
        bestMax = total
        for i in range(len(nums)-k):
            total = total - nums[i] + nums[i+k]
            bestMax = max(bestMax, total)
        return (bestMax/k)




nums = [9,7,3,5,6,2,0,8,1,9]
k = 6
obj = Solution()
print(obj.findMaxAverage(nums, k))
# accepted 