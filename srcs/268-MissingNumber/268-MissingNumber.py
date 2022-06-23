class Solution:
    def missingNumber(self, nums: List[int]):
        for num in range(len(nums) + 1):
            if num not in nums:
                return num

    def missingNumber(self, nums: List[int]):
        return int(len(nums) * (len(nums) + 1) / 2) - sum(nums)
