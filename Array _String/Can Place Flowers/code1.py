class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        flowerbed_len = len(flowerbed)
        count = 0
        for i in range(flowerbed_len):
            if flowerbed[i] == 1:
                continue

            left_plot_free  = i == 0 or flowerbed[i - 1] == 0
            right_plot_free = i == flowerbed_len - 1 or flowerbed[i + 1] == 0

            if left_plot_free and right_plot_free:
                flowerbed[i] = 1
                count += 1

        if n <= count:
            return True
        else:
            return False



flowerbed = [0,0,0,0,1,0,1]
n = 2
obj = Solution()
print(obj.canPlaceFlowers(flowerbed, n))