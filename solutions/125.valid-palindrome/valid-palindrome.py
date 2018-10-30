class Solution:
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
        