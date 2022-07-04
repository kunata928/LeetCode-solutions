from collections import OrderedDict, Counter


class Solution:
    def firstUniqChar(self, s):
        dict_s = dict()
        for letter in s:
            dict_s[letter] = dict_s.get(letter, 0) + 1
        for i, l in zip(range(len(s)), s):
            if dict_s[l] == 1:
                return i
        return -1

    def firstUniqChar1(self, s):
        dict_s = dict()
        for letter in s:
            dict_s[letter] = dict_s.get(letter, 0) + 1
        for i in range(len(s)):
            if dict_s[s[i]] == 1:
                return i
        return -1

    def firstUniqChar2(self, s):
        for key, val in OrderedDict(Counter(s)).items():
            if val == 1:
                return s.index(key)
        return -1


print(Solution.firstUniqChar2(Solution, "leetcode"))