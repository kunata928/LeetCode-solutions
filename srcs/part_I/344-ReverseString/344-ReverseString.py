class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def reverseString1(self, s):
        s[:] = s[::-1]

s = list("012345")
print(s)
Solution.reverseString(Solution, s)
print(s)