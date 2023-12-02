class Solution:
    def reverseVowels(self, s: str) -> str:
        text = list(s)
        vowels = ""
        indexofvowels = []
        for i in range(len(text)):
            if text[i] == "a" or text[i]== "i" or text[i] == "o" or text[i] == "u" or text[i] == "e" or text[i] == "A" or text[i]== "I" or text[i] == "O" or text[i] == "U" or text[i] == "E":
                vowels += text[i]
                indexofvowels.append(i)
        revVowels = vowels[::-1]
        for i in range(len(vowels)):
            text[indexofvowels[i]] = revVowels[i]
        
        return ''.join(e for e in text)

            

s = "leetcode"
# print(list(s))
obj = Solution()
print(obj.reverseVowels(s))