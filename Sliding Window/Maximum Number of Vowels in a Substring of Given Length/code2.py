class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        num_v = 0
        for l in s[:k]:
            if l in vowels:
                num_v += 1
        max_v = num_v
        for i in range(k, len(s)):
            x = s[i-k]
            y = s[i]
            if x in vowels:
                num_v -= 1
            if y in vowels:
                num_v += 1
                max_v = max(max_v, num_v)
        return max_v

s = "weallloveyou"
# print(s.count("i"))
k = 7
obj = Solution()
print(obj.maxVowels(s, k))