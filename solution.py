import re


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = -1
        j = 0
        # nums[0....i]表示非0元素的数列,初始值i=-1
        while j <= n - 1:
            if nums[j] != 0:
                i += 1
                nums[i] = nums[j]
            j += 1
        for k in range(i + 1, n):
            nums[k] = 0

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        i = -1
        j = 0
        while j <= n - 1:
            if nums[j] != val:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n
        # nums[0,i]为非重复数列
        i = 0
        j = i + 1
        while j <= n - 1:
            if nums[j] != nums[i]:
                # 指向同一个元素不需要赋值
                if i + 1 != j:
                    nums[i + 1] = nums[j]
                i += 1
            j += 1
        return i + 1

    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if (n <= 2):
            return n
        # nums[0...i]是符合要求的，
        i = 1
        k = i - 1
        j = i + 1

        while j <= n - 1:
            if (nums[j] != nums[i]) or (nums[j] == nums[i] and nums[j] != nums[k]):
                k = i
                nums[i + 1] = nums[j]
                i += 1
            j += 1

        return i + 1

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

    def findKthLargest(self, nums, k):
        n = len(nums)
        if (k > n):
            return
        index = self.quickSort(nums, 0, n - 1, k)
        return nums[index]

    def quickSort(self, nums, l, r, k):
        if l >= r:
            return l
        p = self.partition(nums, l, r)
        if p + 1 == k:
            return p
        if p + 1 > k:
            return self.quickSort(nums, l, p - 1, k)
        else:
            return self.quickSort(nums, p + 1, r, k)

    def partition(self, nums, l, r):
        v = nums[l]
        j = l
        i = l + 1
        while i <= r:
            if nums[i] >= v:
                nums[j + 1], nums[i] = nums[i], nums[j + 1]
                j += 1
            i += 1
        nums[l], nums[j] = nums[j], nums[l]
        return j

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        idx1 = m - 1
        idx2 = n - 1
        curr = m + n - 1
        while idx1 >= 0 and idx2 >= 0:
            if nums1[idx1] >= nums2[idx2]:
                nums1[curr] = nums1[idx1]
                idx1 -= 1
            else:
                nums1[curr] = nums2[idx2]
                idx2 -= 1
            curr -= 1
        while idx2 >= 0:
            nums1[curr] = nums2[idx2]
            idx2 -= 1
            curr -= 1
        return

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

    def isPalindrome(self, s):
        result = True
        if len(s) == 0:
            return result
        s = self.cleanString(s)
        if s is None:
            return result
        idx1 = 0
        idx2 = len(s) - 1
        while idx1 < idx2:
            print(s[idx1], s[idx2])
            if s[idx1] == s[idx2]:
                idx1 += 1
                idx2 -= 1
            else:
                result = False
                break
        return result

    def cleanString(self, s):
        pattern = re.compile(r'[a-zA-Z0-9]')
        if re.findall(pattern, s):
            return ''.join(re.findall(pattern, s)).lower()

