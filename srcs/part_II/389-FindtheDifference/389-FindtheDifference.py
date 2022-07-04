class Solution:
    def findTheDifference(self, s, t):
        for letter in t:
            if s.count(letter) != t.count(letter):
                return letter

    def findTheDifference1(self, s, t):
        x = 0
        for c in s + t:
            x ^= ord(c)
            print(x)
        return chr(x)


print(Solution.findTheDifference1(Solution, "asdf", "agsdf"))

