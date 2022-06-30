from functools import reduce


class Solution:
    def isHappy(self, n: int) -> bool:
        n = reduce(lambda x, y: x + y, list(map(lambda x: x*x, list(map(int, str(n))))))
        while n > 9:
            n = reduce(lambda x, y: x + y, list(map(lambda x: x*x, list(map(int, str(n))))))
        print(True if n == 1 or n == 7 else False)


Solution.isHappy(Solution, 19)