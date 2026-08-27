# Last updated: 8/27/2026, 9:24:05 AM
1class Solution:
2    def lexGreaterPermutation(self, s: str, target: str) -> str:
3        n = len(s)
4        for i in range(n - 1, -1, -1):
5            count = [0] * 26
6            for ch in s:
7                count[ord(ch) - ord('a')] += 1
8            possible = True
9
10            for j in range(i):
11                x = ord(target[j]) - ord('a')
12
13                if count[x] == 0:
14                    possible = False
15                    break
16
17                count[x] -= 1
18
19            if not possible:
20                continue
21            x = ord(target[i]) - ord('a')
22
23            for c in range(x + 1, 26):
24                if count[c] > 0:
25                    result = list(target[:i])
26                    result.append(chr(c + ord('a')))
27                    count[c] -= 1
28                    for d in range(26):
29                        result.extend([chr(d + ord('a'))] * count[d])
30
31                    return ''.join(result)
32
33        return ""