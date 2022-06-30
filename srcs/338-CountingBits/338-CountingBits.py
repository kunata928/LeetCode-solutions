class Solution:
    def countBits(self, n):
        counter = [0]
        for i in range(1, n + 1):
            print(i, counter[i // 2])
            counter.append(counter[i // 2] + i % 2)
        return counter

    def countBits1(self, n: int) -> List[int]:
        counter = [0]
        for i in range(1, n + 1):
            counter.append(counter[i >> 1] + i % 2)
        return counter


print(Solution.countBits(Solution, 7))