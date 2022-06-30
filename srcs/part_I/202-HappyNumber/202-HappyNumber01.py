class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        seen.add(n)
        while n > 9:
            n = sum([int(num) * int(num) for num in str(n)])
            if n in seen:
                return False
            seen.add(n)
        return True if n == 1 or n == 7 else False


Solution.isHappy(Solution, 19)