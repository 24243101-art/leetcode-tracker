# Last updated: 7/9/2026, 10:11:11 AM
class Solution(object):
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        num1, num2 = num1[::-1], num2[::-1]

        for i in range(m):
            for j in range(n):
                res[i + j] += int(num1[i]) * int(num2[j])
                if res[i + j] >= 10:
                    res[i + j + 1] += res[i + j] // 10
                    res[i + j] %= 10

        while len(res) > 1 and res[-1] == 0:
            res.pop()

        return ''.join(map(str, res[::-1]))
