class Solution:
    def findDifference(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        
        result1 = list(set1 - set2)
        result2 = list(set2 - set1)
        
        return [result1, result2]



nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
obj = Solution()
print(obj.findDifference(nums1, nums2)) 