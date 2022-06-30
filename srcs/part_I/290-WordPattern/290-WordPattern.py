class Solution:
    def wordPattern(self, pattern, s):
        p = pattern
        s_arr = s.split()
        return len(set(zip(p, s_arr))) == len(set(p)) == len(set(s_arr)) and len(p) == len(s_arr)

    def wordPattern1(self, pattern, s): #incorrect
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


print(Solution.wordPattern(Solution, "aaaa", "dog cat cat dog"))