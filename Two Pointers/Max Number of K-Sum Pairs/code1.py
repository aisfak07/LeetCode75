class Solution:
    def maxOperations(self, nums, k):
        left = 0
        right = len(nums)-1
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0 and nums[i]<k:
                numTosearch = k - nums[i]
                for j in range(i+1, len(nums)):
                    if nums[j] == numTosearch:
                        count += 1
                        nums[i] = 0
                        nums[j] = 0
                        break
                        
                    else:
                        continue
            else:
                continue
                
        
        return count



nums = [2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2]
# print(len(nums))
k = 3
obj = Solution()
print(obj.maxOperations(nums, k))

# 46/ 51 test cases passad (Time Limit Exceed Error)