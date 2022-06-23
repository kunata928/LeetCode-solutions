class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = sum([int(n) for n in str(num)])
        return(num)

    def addDigits1(self, num):
        return num if num == 0 else num % 9 or 9


print(Solution.addDigits1(Solution, 2225))

