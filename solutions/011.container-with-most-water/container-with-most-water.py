class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_volume = 0
        n = len(height)
        if n == 2:
            max_volume = height[0] if height[0] < height[1] else height[1]
            return max_volume
        idx1 = 0
        idx2 = n - 1
        while idx1 < idx2:
            h = height[idx1] if height[idx1] < height[idx2] else height[idx2]
            max_volume = max_volume if max_volume > h * (idx2 - idx1) else h * (idx2 - idx1)
            if height[idx1] < height[idx2]:
                idx1 += 1
            else:
                idx2 -= 1
        return max_volume