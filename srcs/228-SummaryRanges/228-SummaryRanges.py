class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return []
        res = list()
        start, prev = nums[0], nums[0] - 1
        nums.append(nums[len(nums)-1] + 2)
        for num in nums:
            if num != prev + 1:
                if start == prev:
                    res.append(str(start))
                    start = num
                else:
                    res.append(str(start)+"->"+str(prev))
                    start = num
            prev = num
        return res

    def summaryRanges1(self, nums):
        ranges, r = [], []
        for n in nums:
            if n-1 not in r:
                r = []
                ranges += r,
            r[1:] = n,
            print(n,)
        return ['->'.join(map(str, r)) for r in ranges]

print(Solution.summaryRanges1(Solution, [0,2,3,4,6,8,9]))