class Solution:
    def canConstruct(self, ransomNote, magazine):
        dict_mag = dict()
        for m in magazine:
            dict_mag[m] = dict_mag.get(m, 0) + 1
        for r in ransomNote:
            if dict_mag.get(r) and dict_mag.get(r, 0) - 1 >= 0:
                dict_mag[r] -= 1
            else:
                return False
        return True

    def canConstruct1(self, ransomNote, magazine):
        return all(ransomNote.count(letter) <= magazine.count(letter) for letter in ransomNote)

    def canConstruct2(self, ransomNote, magazine):
        return all(ransomNote.count(c) <= magazine.count(c) for c in string.ascii_lowercase)