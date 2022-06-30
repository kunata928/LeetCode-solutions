class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1).intersection(set(nums2)))

    def intersection1(self, nums1, nums2):
        return list(set(nums1) & set(nums2))

    def intersection2(self, nums1, nums2):
        res = []
        for i in nums1:
            if i not in res and i in nums2:
                res.append(i)
        return res


print(Solution.intersection1(Solution, [1, 2, 2, 1], [2, 2]))