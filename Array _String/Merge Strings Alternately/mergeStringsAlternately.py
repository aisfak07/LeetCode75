class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        zipped = ""
        for i in range(min(len(word1), len(word2))):
            zipped += word1[i]
            zipped += word2[i]
            i+= 1
        
        zipped += word1[i:] +word2[i:]

        return zipped



x = Solution()
word1= "abc"
word2 ="p"
z = x.mergeAlternately(word1, word2)
print(z)


