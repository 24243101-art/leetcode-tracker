# Last updated: 7/29/2026, 3:18:28 PM
1from collections import Counter
2
3class Solution:
4    def smallestPalindrome(self, s: str, k: int) -> str:
5        freq = Counter(s)
6        odd_chars = [c for c, f in freq.items() if f % 2 == 1]
7        if len(odd_chars) > 1:
8            return ""
9        
10        half = []
11        for c in sorted(freq.keys()):
12            half.extend([c] * (freq[c] // 2))
13        half = "".join(half)
14        middle = odd_chars[0] if odd_chars else ""
15        
16        n = len(half)
17        
18        fact = [1] * (n+1)
19        for i in range(1, n+1):
20            fact[i] = fact[i-1] * i
21        
22        counter = Counter(half)
23        total = sum(counter.values())
24        denom = 1
25        for v in counter.values():
26            denom *= fact[v]
27        total_perms = fact[total] // denom
28        
29        if k > total_perms:
30            return ""
31        
32        result_half = []
33        for _ in range(n):
34            for c in sorted(counter.keys()):
35                if counter[c] == 0:
36                    continue
37                cnt = total_perms * counter[c] // total
38                if k <= cnt:
39                    result_half.append(c)
40                    counter[c] -= 1
41                    total -= 1
42                    total_perms = cnt
43                    break
44                else:
45                    k -= cnt
46            else:
47                return ""
48        
49        left = "".join(result_half)
50        return left + middle + left[::-1]
51