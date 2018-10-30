class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        i, j = 0, 0
        if size is 0:
            return size
        while j <= size - 1:
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i+1