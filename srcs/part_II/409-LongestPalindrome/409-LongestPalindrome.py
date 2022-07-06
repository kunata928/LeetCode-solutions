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


strs = [
"civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
    # "aa",
    # "aabbcd",
    # "aaaaabbcd",
    # "aaaabbbccd"
]
for s in strs:
    print(s, Solution.longestPalindrome(Solution, s))

#len include all even letters and len odd letter - 1 (and extra 1, if odd exist)