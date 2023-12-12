class Solution:
    def increasingTriplet(self, nums):
        first = second = third = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False




nums = [20,100,10,12,5,13]
obj = Solution()
print(obj.increasingTriplet(nums))
# first = second = float('inf')
# print(first, second)