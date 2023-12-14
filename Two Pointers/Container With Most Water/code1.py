class Solution:
    def maxArea(self, height):
        l = 0
        r = len(height)-1
        area = 0
        for i in range(len(height)):
            if height[l] > height[r]:
                newArea = (r-l)*height[r]
                if area < newArea:
                    area = newArea
                r -= 1
            elif height[l] <= height[r]:
                newArea = (r-l)*height[l]
                if area < newArea:
                    area = newArea
                l += 1
        return area


height = [6,2,5,8,3,6]
obj = Solution()
print(obj.maxArea(height))