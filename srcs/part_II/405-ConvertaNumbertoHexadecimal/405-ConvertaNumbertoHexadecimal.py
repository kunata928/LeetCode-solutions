class Solution:
    def toHex(self, num):
        num_hex = ""
        hex_alp = "0123456789abcdef"
        if num == 0:
            return '0'
        if num < 0:
            num += 2 ** 32
        while num > 0:
            num_hex += hex_alp[num % 16]
            num //= 16
        return num_hex[::-1]


print(Solution.toHex(Solution, 26))