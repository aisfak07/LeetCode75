
class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        boolList = []
        maxcandy = max(candies)
        for i in range(len(candies)):
            x = candies[i] + extraCandies
            if x >= maxcandy:
                boolList.append(True)
            else:
                boolList.append(False)
        
        return boolList




candies = [2,3,5,1,3]
extraCandies = 3

obj = Solution()
print(obj.kidsWithCandies(candies, extraCandies))