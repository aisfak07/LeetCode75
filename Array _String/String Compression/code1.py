class Solution:
    def compress(self, chars):
        s = []
        listy = list(set(chars))
        for i in listy:
            count = 0
            for j in chars:
                if i == j:
                    count += 1
            s.append(i)
            if count > 1:
                if count>=10:
                    a = str(count/10).split(".")
                    for i in a:
                        s.append(i)
                else:
                    s.append(count)
        
        print(chars)
        return len(chars)
        


chars = ["a","b","b","c","c","c","d","d","d","d","d","d","d","d","d","d","d","d"]
obj = Solution()
print(obj.compress(chars))
# list_set = set(chars)
# print(list_set)
