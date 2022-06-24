class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        pos_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[pos_zero] = nums[pos_zero], nums[i]
                pos_zero += 1


nums = [1, 2, 3, 0, 0, 0 , 4, 0, 5]
Solution.moveZeroes(Solution, nums)
print(nums)
