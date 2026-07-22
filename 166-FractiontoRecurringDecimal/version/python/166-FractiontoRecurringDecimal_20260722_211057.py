# Last updated: 7/22/2026, 9:10:57 PM
1class Solution:
2    def fractionToDecimal(self, numerator, denominator):
3        if numerator == 0:
4            return "0"
5        result = []
6        if (numerator < 0) ^ (denominator < 0):
7            result.append("-")
8        numerator = abs(numerator)
9        denominator = abs(denominator)
10        result.append(str(numerator // denominator))
11        remainder = numerator % denominator
12        if remainder == 0:
13            return "".join(result)
14        result.append(".")
15        remainder_map = {}
16        while remainder:
17            if remainder in remainder_map:
18                index = remainder_map[remainder]
19                result.insert(index, "(")
20                result.append(")")
21                break
22            remainder_map[remainder] = len(result)
23            remainder *= 10
24            result.append(str(remainder // denominator))
25            remainder %= denominator
26
27        return "".join(result)