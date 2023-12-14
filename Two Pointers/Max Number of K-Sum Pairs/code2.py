class Solution:
    def maxOperations(self, nums, k):
        count = 0
        l = 0
        r = len(nums)-1
        while(l<r):
            if nums[l] < k:
                if nums[r] < k:
                    if nums[l] + nums[r] == k:
                        count += 1
                        del nums[r]
                        del nums[l]
                        r = len(nums) -1
                    else:
                        r -= 1
                else:
                    del nums[r]
                    r = len(nums) -1
            else:
                del nums[l]
                r = len(nums) -1
        
        return count



nums = [3,1,3,4,3]
# print(len(nums))
k = 6
obj = Solution()
print(obj.maxOperations(nums, k))

# time limit exceeds
