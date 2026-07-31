# Last updated: 7/31/2026, 10:13:06 PM
1class Solution:
2    def minimumPushes(self, word: str) -> int:
3        freq = [0] * 26
4
5        for ch in word:
6            freq[ord(ch) - ord('a')] += 1
7
8        freq.sort(reverse=True)
9
10        ans = 0
11
12        for i in range(26):
13            if freq[i] == 0:
14                break
15            ans += freq[i] * (i // 8 + 1)
16
17        return ans