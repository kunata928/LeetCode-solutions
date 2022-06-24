class Solution:
    def wordPattern(self, pattern, s):
        letter_dict = dict()
        s_arr = s.split()
        if len(pattern) != len(s_arr):
            return False
        for i in range(len(s_arr)):
            if not letter_dict.get(pattern[i]):
                letter_dict[pattern[i]] = s_arr[i]
            else:
                if letter_dict[pattern[i]] != s_arr[i]:
                    return False
        return True


print(Solution.wordPattern(Solution, "abba", "dog cat cat dog"))