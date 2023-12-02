class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left = 0 
        right = len(s)-1
        vowels = "aeiouAEIOU"
        while left < right:
            if s[left] not in vowels:
                left += 1
                continue
            elif s[right] not in vowels:
                right -= 1
                continue
            s[left], s[right] = s[right], s[left]
            left+=1
            right -=1

        
        return ''.join(s)

            

s = "leetcode"
# print(list(s))
obj = Solution()
print(obj.reverseVowels(s))