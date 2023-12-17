class Solution:
    def findMaxAverage(self, nums, k) :
        max_sum = 0
        current_sum = 0

        # Initialize the sum of the first window
        for i in range(k):
            current_sum += nums[i]

        # Slide the window through the array
        if k == len(nums):
            max_sum = current_sum
        elif k == 1:
            max_sum = max(nums)
        elif k > 1:
            for i in range(k, len(nums)):
                current_sum += nums[i] - nums[i - k]
                max_sum = max(max_sum, current_sum)
        else:
            max_sum = current_sum

        return max_sum/k

nums = [9,7,3,5,6,2,0,8,1,9]
k = 6
obj = Solution()
print(obj.findMaxAverage(nums, k))

#120 test cases passad