class Solution:
    def longestPalindrome(self, s):
        res = 0
        max_odd = 0
        dict_s = dict()
        for letter in s:
            dict_s[letter] = dict_s.get(letter, 0) + 1
        for key, val in dict_s.items():
            print(key, val)
            if val % 2 == 0:
                res += val
            else:
                res += val - 1
                max_odd = 1
        return res + max_odd

    def longestPalindrome1(self, s):
        ss = set()
        for letter in s:
            if letter not in ss:
                ss.add(letter)
            else:
                ss.remove(letter)
        if len(ss) != 0:
            return len(s) - len(ss) + 1
        else:
            return len(s)


strs = [
"civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
    # "aa",
    # "aabbcd",
    # "aaaaabbcd",
    # "aaaabbbccd"
]
for s in strs:
    print(s, Solution.longestPalindrome1(Solution, s))

#len include all even letters and len odd letter - 1 (and extra 1, if odd exist)