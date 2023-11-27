class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        newStr = ""
        for i in range(min(len(str1), len(str2))):
            if str1[i] == str2[i]:
                if str1[i] not in newStr:
                    newStr += str1[i]
        
        return newStr


str1 = "LEET"
str2 = "CODE"
z = Solution()
print(z.gcdOfStrings(str1, str2))