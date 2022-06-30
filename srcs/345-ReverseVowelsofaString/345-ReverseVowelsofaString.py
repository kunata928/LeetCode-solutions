class Solution:
    def reverseVowels(self, s):
        vowels = 'aeiouAEIOU' #('a', 'i', 'o', 'e', 'u', 'A', 'I', 'O', 'E', 'U')
        strr = list(s)
        i = 0
        right = len(strr) - 1
        while i < len(strr):
            if strr[i] in vowels:
                while right > i and (strr[right] not in vowels):
                    right -= 1
                if strr[right] in vowels and right > i:
                    strr[i], strr[right] = strr[right], strr[i]
                    right -= 1
            i += 1
        return "".join(strr)
    

print(Solution.reverseVowels(Solution, "ai"))