class Solution:
    def containsDuplicate(self, nums) -> bool:
        return len(set(nums)) != len(nums)


print(Solution.containsDuplicate(Solution, [1, 2, 3, 1]))