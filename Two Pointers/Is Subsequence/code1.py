class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        positions = []
        flag = 0
        for i in range(len(s)):
            if s[i] in t:
                for j in range(len(t)):
                    if s[i] == t[j]:
                        positions.append(j)
            else:
                return False
        
        
        for i in range(len(positions)-1):
            if not positions[i] < positions[i+1]:
                flag += 1
            
        if flag > 0:
             return False
        else:
            return True



s = "abc"
t = "ahbgdc"
obj = Solution()
print(obj.isSubsequence(s, t))

# 16 test cases passed