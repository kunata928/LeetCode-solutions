class Solution:
    def isSubsequence(self, s, t):
        for i in range(len(s)):
            try:
                index = t.index(s[i])
            except ValueError:
                return False
            t = t[index + 1:]
        return True