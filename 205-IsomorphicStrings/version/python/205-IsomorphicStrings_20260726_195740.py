# Last updated: 7/26/2026, 7:57:40 PM
1class Solution:
2    def isIsomorphic(self, s: str, t: str) -> bool:
3        mapST = {}
4        mapTS = {}
5
6        for i in range(len(s)):
7            c1 = s[i]
8            c2 = t[i]
9
10            if c1 in mapST:
11                if mapST[c1] != c2:
12                    return False
13            else:
14                mapST[c1] = c2
15
16            if c2 in mapTS:
17                if mapTS[c2] != c1:
18                    return False
19            else:
20                mapTS[c2] = c1
21
22        return True