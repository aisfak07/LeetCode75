class Solution:
    def reverseWords(self, s: str) -> str:
        splittedArray = s.split(' ')
        textArray = []
        for i in splittedArray:
            if i == "":
                continue
            else:
                textArray.append(i)
        return " ".join(textArray[::-1])

s = "the sky is blue"
s1 = "  hello  world  "
obj = Solution()
print(obj.reverseWords(s1))