class Solution:
    
    def __init__(self):
        self.yuanyin = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        character_list = list(s)
        n = len(s)
        if n <= 1:
            return s
        idx1 = 0
        idx2 = n - 1
        while idx1 < idx2:
            if not self.isYuanyin(s[idx1]):
                idx1 += 1
            if not self.isYuanyin(s[idx2]):
                idx2 -= 1
            if self.isYuanyin(s[idx1]) and self.isYuanyin(s[idx2]):
                character_list[idx1], character_list[idx2] = character_list[idx2], character_list[idx1]
                idx1 += 1
                idx2 -= 1
        return "".join(character_list)
        
    def isYuanyin(self, c):
        return c in self.yuanyin
