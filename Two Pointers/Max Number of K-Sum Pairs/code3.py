class Solution:
    def maxOperations(self, nums, k):
        count = 0
        l = 0
        r = len(nums)-1
        while(l<r):
            if nums[r]> k:
                r -= 1
            elif nums[l]>k:
                l += 1
            else:    
                if nums[l] + nums[r] == k:
                    count += 1
                    l+=1
                    r-=1
                elif nums[l] + nums[r] > k:
                    r-=1
                else:
                    l+=1
        
        return count



nums = [3,1,3,4,3]
# print(len(nums))
k = 6
obj = Solution()
print(obj.maxOperations(nums, k))

# time limit exceeds
