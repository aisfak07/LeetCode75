class Solution:
    def largestAltitude(self, gain):
        preGain = [0 for i in range(len(gain)+1)]
        for i in range(len(gain)):
            preGain[i+1] = preGain[i] + gain[i]
        
        return max(preGain)



gain = [-5,1,5,0,-7]
gain2 = [-4,-3,-2,-1,4,3,2]
obj = Solution()
print(obj.largestAltitude(gain2)) 