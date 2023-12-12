class Solution:
    def compress(self, chars):
        i = j = k = 0
        if len(chars) == 1:
            return 1
        else:
            while(k < len(chars)):
                while(j < len(chars) and chars[k] == chars[j]):
                    j += 1
                
                chars[i] = chars[k]
                i += 1
                if j-k > 1:
                    count = str(j - k)
                    for x in count:
                        chars[i] = x
                        i += 1
                
                k = j
            
            chars = chars[:i]
            return len(chars)


        # print(s)
        # return len(s)
        


chars = ["a","b","b","c","c","c","d","d","d","d","d","d","d","d","d","d","d","d"]
obj = Solution()
print(obj.compress(chars))
# list_set = set(chars)
# print(list_set)
