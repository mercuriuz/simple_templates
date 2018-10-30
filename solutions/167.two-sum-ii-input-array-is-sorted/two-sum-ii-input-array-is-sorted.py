class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx1 = 0
        idx2 = len(numbers) - 1
        while idx1 < idx2:
            sum = numbers[idx1] + numbers[idx2]
            if sum == target:
                break
            if sum > target:
                idx2 -= 1
            if sum < target:
                idx1 += 1

        return idx1 + 1, idx2 + 1
        