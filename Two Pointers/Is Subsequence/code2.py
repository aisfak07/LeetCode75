class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0
        for i in t:
            try:
                if i == s[count]:
                    count += 1
            except:
                continue
        
        if len(s) == count:
            return True
        else:
            return False


s = "axc"
t = "ahbgdc"
obj = Solution()
print(obj.isSubsequence(s, t))

# All test cases passed