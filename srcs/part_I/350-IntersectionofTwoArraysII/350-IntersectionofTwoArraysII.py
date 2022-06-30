class Solution:
    def intersect(self, nums1, nums2):
        res = list()
        counts = dict()
        for num in nums1:
            counts[num] = counts.get(num, 0) + 1
        for num in nums2:
            if num in counts and counts[num] > 0:
                counts[num] -= 1
                res.append(num)
        return res


print(Solution.intersect(Solution, [1, 2, 2, 1], [2, 2]))