class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        i = -1
        j = 0
        while j <= n-1:
            if nums[j] is not val:
                i += 1
                nums[i] = nums[j]
            j += 1
        nums = nums[:i+1]
        return len(nums)
        