class Solution:
    def majorityElement(self, nums) -> int:
        average = len(nums) // 2
        d_nums = dict()
        for n in nums:
            if d_nums.get(n):
                d_nums[n] += 1
            else:
                d_nums[n] = 1
            if d_nums[n] > average:
                return n


    def majorityElement01(self, nums) -> int:
        d_nums = dict()
        for n in nums:
            d_nums[n] = d_nums.get(n, 0) + 1
            if d_nums[n] > len(nums) // 2:
                return n



print(Solution.majorityElement(Solution, [1, 1, 2, 3]))