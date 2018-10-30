class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        if size <= 1:
            return
        pivot_start = 0
        pivot_end = size - 1
        idx = 0
        while True:
            if idx >= pivot_end + 1:
                break
            if nums[idx] == 0:
                self.swap(nums, idx, pivot_start)
                idx += 1
                pivot_start += 1
            elif nums[idx] == 2:
                self.swap(nums, idx, pivot_end)
                pivot_end -= 1
            else:
                idx += 1
            
            
    def swap(self, nums, a, b):
        nums[a], nums[b] = nums[b], nums[a]