class Solution:
    def isAnagram(self, s: str, t: str):
        return "".join(sorted(s)) == "".join(sorted(t))

    def isAnagram1(self, s: str, t: str):
        return sorted(s) == sorted(t)

    def isAnagram2(self, s: str, t: str):
        dict_s = dict()
        dict_t = dict()
        for letter in s:
            dict_s[letter] = dict_s.get(letter, 0) + 1
        for letter in t:
            dict_t[letter] = dict_t.get(letter, 0) + 1
        return dict_s == dict_t


s = "anagram"
t = "anagram"
print(Solution.isAnagram2(Solution, s, t))