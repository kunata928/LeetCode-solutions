class Solution:
    def isPerfectSquare(self, num):
        i = 0
        while i * i < num:
            i += 1
        return i * i == num

print(Solution.isPerfectSquare(Solution, 16))