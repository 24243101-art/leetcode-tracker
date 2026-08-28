# Last updated: 8/28/2026, 9:15:03 AM
1class Solution:
2    def buildFullPalindrome(self, firstHalf, centerIndex):
3        secondHalf = firstHalf[::-1]
4        result = firstHalf
5        if centerIndex != -1:
6            result += chr(ord('a') + centerIndex)
7        result += secondHalf
8        return result
9    def lexPalindromicPermutation(self, s, target):
10        totalLen = len(s)
11        freq = [0] * 26
12        for ch in s:
13            freq[ord(ch) - ord('a')] += 1
14        centerIndex = -1
15        for i in range(26):
16            if freq[i] % 2 == 1:
17                if centerIndex != -1:
18                    return ""
19                centerIndex = i
20            freq[i] //= 2
21        nHalf = totalLen // 2
22        firstHalf = ""
23        pos = 0
24        madeGreaterPrefix = False
25        while pos < nHalf and not madeGreaterPrefix:
26            want = ord(target[pos]) - ord('a')
27            candidate = want
28            while candidate < 26 and freq[candidate] == 0:
29                candidate += 1
30            if candidate == 26:
31                break
32            if candidate > want:
33                madeGreaterPrefix = True
34            freq[candidate] -= 1
35            firstHalf += chr(ord('a') + candidate)
36            pos += 1
37        if pos == nHalf and not madeGreaterPrefix:
38            palindrome = self.buildFullPalindrome(
39                firstHalf,
40                centerIndex
41            )
42            if palindrome > target:
43                return palindrome
44        if not madeGreaterPrefix:
45            pos -= 1
46            while pos >= 0:
47                currentCharIdx = (
48                    ord(firstHalf[pos]) - ord('a')
49                )
50                freq[currentCharIdx] += 1
51                nextCandidate = currentCharIdx + 1
52                while (
53                    nextCandidate < 26
54                    and freq[nextCandidate] == 0
55                ):
56                    nextCandidate += 1
57                if nextCandidate < 26:
58                    freq[nextCandidate] -= 1
59                    firstHalf = (
60                        firstHalf[:pos]
61                        + chr(ord('a') + nextCandidate)
62                        + firstHalf[pos + 1:]
63                    )
64                    break
65                pos -= 1
66            if pos < 0:
67                return ""
68            madeGreaterPrefix = True
69            pos += 1
70        for letter in range(26):
71            while freq[letter] > 0 and pos < nHalf:
72                firstHalf = (
73                    firstHalf[:pos]
74                    + chr(ord('a') + letter)
75                    + firstHalf[pos + 1:]
76                )
77                freq[letter] -= 1
78                pos += 1
79        result = self.buildFullPalindrome(
80            firstHalf,
81            centerIndex
82        )
83        if result > target:
84            return result
85        return ""