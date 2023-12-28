class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        splittedString = list(s)
        i = 0
        x = k
        subString = splittedString[:k]
        max_count = 0
        vowels = "aeiou"
        n = len(splittedString)-k
        while(i <= n):
            count = 0
            for j in subString:
                if j.upper() in vowels.upper():
                    count += 1
            
            max_count = max(max_count, count)
            try:
                subString.remove(s[i])
                subString.append(s[x])
            except:
                break
            i += 1
            x += 1
        
        
        return max_count



s = "weallloveyou"
# print(s.count("i"))
k = 7
obj = Solution()
print(obj.maxVowels(s, k))
# Time Limit exceeds. 98 test cases passad