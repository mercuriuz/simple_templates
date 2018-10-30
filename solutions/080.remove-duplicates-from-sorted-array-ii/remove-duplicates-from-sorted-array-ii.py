class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size <= 1:
            return size
        i, j = 0, 1
        if nums[0] == nums[1]:
            i, j = 1, 2
        while j <= size - 1:
            if nums[j] != nums[i]:
                # 指向同一个元素不需要赋值
                if j < size - 1 and nums[j + 1] == nums[j]:
                    nums[i + 1] = nums[j]
                    nums[i + 2] = nums[j]
                    i += 2
                else:
                    nums[i + 1] = nums[j]
                    i += 1
            j += 1
        return i + 1