# Last updated: 8/13/2026, 9:49:27 PM
1class Solution:
2    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
3
4        n = len(s)
5        tree = [None] * (4 * n)
6
7        def merge(a, b):
8            if a is None:
9                return b
10            if b is None:
11                return a
12
13            left_char = a[0]
14            right_char = b[1]
15
16            length = a[5] + b[5]
17            prefix = a[2]
18            if a[2] == a[5] and a[1] == b[0]:
19                prefix = a[5] + b[2]
20            suffix = b[3]
21            if b[3] == b[5] and a[1] == b[0]:
22                suffix = b[5] + a[3]
23            best = max(a[4], b[4])
24            if a[1] == b[0]:
25                best = max(best, a[3] + b[2])
26
27            return (left_char, right_char, prefix, suffix, best, length)
28
29        def build(node, left, right):
30            if left == right:
31                ch = s[left]
32                tree[node] = (ch, ch, 1, 1, 1, 1)
33                return
34
35            mid = (left + right) // 2
36
37            build(node * 2, left, mid)
38            build(node * 2 + 1, mid + 1, right)
39
40            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])
41
42        def update(node, left, right, index, ch):
43            if left == right:
44                tree[node] = (ch, ch, 1, 1, 1, 1)
45                return
46
47            mid = (left + right) // 2
48
49            if index <= mid:
50                update(node * 2, left, mid, index, ch)
51            else:
52                update(node * 2 + 1, mid + 1, right, index, ch)
53
54            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])
55
56        build(1, 0, n - 1)
57
58        answer = []
59
60        for ch, index in zip(queryCharacters, queryIndices):
61            update(1, 0, n - 1, index, ch)
62
63            answer.append(tree[1][4])
64
65        return answer