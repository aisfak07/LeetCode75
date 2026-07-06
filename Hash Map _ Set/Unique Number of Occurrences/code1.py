class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        count = {}
        for i in arr:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        occurrences = set()
        for key in count:
            if count[key] in occurrences:
                return False
            occurrences.add(count[key])

        return True




arr = [1,1,1,1,2,2,2,3,3,3,3,4]
obj = Solution()
print(obj.uniqueOccurrences(arr)) 