class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0

    def isPowerOfThree1(self, n):
        while n > 2:
            if n % 3 > 0:
                return False
            n = n / 3
        return n == 1