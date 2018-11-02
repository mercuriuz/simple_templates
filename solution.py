import re
from functools import *

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

    def groupAnagrams(self, strs):
        hash_dict = dict()
        for item in strs:
            item_hash = 1
            for char in item:
                item_hash *= (ord(char) + 10000)
            hash_dict[item_hash] = hash_dict.get(item_hash, []) + [item]
        res = [value for value in hash_dict.values()]
        return res

    def longestPalindrome(self, s):
        start, length, size = 0, 0, len(s)
        if size <= 1 or s == s[::-1]:
            return s
        for i in range(size):
            if i - length - 1 >= 0 and s[i-length-1:i+1] == s[i-length-1:i+1][::-1]:
                start = i - length - 1
                length += 2
                continue
            if i - length >= 0 and s[i-length:i+1] == s[i-length:i+1][::-1]:
                start = i - length
                length += 1
        return s[start:start+length]

    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        mid = len(nums) // 2
        i = 1
        j = 1
        res = False
        while mid - i >= 0 or mid + j <= len(nums) - 1:
            print(nums[mid - i], nums[mid], nums[mid+j], mid - i, mid, mid + j)
            if nums[mid - i] < nums[mid] < nums[mid+j]:
                res = True
                break
            elif nums[mid - i] >= nums[mid] >= nums[mid+j]:
                mid = mid + j
                i += 3
            elif nums[mid - i] >= nums[mid] and nums[mid] <= nums[mid+j]:
                i += 1
            elif nums[mid - i] <= nums[mid] and nums[mid] >= nums[mid+j]:
                j += 1
        return res

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = l1
        cn = 0
        while l1 and l2:
            res = cn + (l1.val) + (l2.val)
            cn, val = res // 10, res % 10
            l1.val = val
            prev, l1, l2 = l1, l1.next, l2.next
        l = l1 or l2
        prev.next = l
        while l and cn:
            res = cn + l.val
            cn, val = res // 10, res % 10
            l.val = val
            prev, l = l, l.next
        if cn:
            prev.next = ListNode(cn)
        return dummy.next

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

if __name__ == '__main__':
    solution = Solution()
    nums = [2,1,5,0,4,6]
    res = solution.increasingTriplet(nums)
    print(res)