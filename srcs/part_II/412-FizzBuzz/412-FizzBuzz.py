class Solution:
    def fizzBuzz(self, n):
        res = [str(i) for i in range(1, n+1)]
        for i in range(2, n, 3):
            res[i] = "Fizz"
        for i in range(4, n, 5):
            res[i] = "Buzz"
        for i in range(14, n, 15):
            res[i] = "FizzBuzz"
        return res

    def fizzBuzz1(self, n):
        res = list()
        for i in range(1, n+1):
            if i % 15 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res

    def fizzBuzz2(self, n):
        # list comprehension with string rule of FizzBuzz
        list_of_output = ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n + 1)]
        return list_of_output


# print(Solution.fizzBuzz1(Solution, 16))