class Solution:
    def longestOnes(self, nums, k):
        left, right = 0, 0
        count = 0
        max_length = 0

        while right < len(nums):
            if nums[right] == 1:
                right += 1
                max_length = max(max_length, right - left)
            elif count < k:
                if nums[right] == 0:
                    count += 1
                right += 1
                max_length = max(max_length, right - left)
            else:
                if nums[left] == 0:
                    count -= 1
                left += 1

        return max_length

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
obj = Solution()
print(obj.longestOnes(nums, k))