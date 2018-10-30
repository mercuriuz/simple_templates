class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        pivot = -1
        if size <= 1:
            return
        while True:
            if nums[pivot] is 0:
                nums.pop(pivot)
                nums.append(0)
            pivot -= 1
            if pivot < -size:
                break