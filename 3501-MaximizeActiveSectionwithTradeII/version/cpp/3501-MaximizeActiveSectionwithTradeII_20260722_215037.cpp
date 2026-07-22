// Last updated: 7/22/2026, 9:50:37 PM
1class Solution {
2public:
3    struct SegTree {
4        vector<int> tree;
5        vector<int>* arr;
6
7        SegTree(vector<int>& a) {
8            arr = &a;
9            tree.assign(4 * a.size(), 0);
10            build(0, a.size() - 1, 1);
11        }
12
13        void build(int l, int r, int i) {
14            if (l == r) {
15                tree[i] = 0;
16                return;
17            }
18
19            int mid = (l + r) / 2;
20            build(l, mid, i * 2);
21            build(mid + 1, r, i * 2 + 1);
22            updateNode(l, r, i);
23        }
24
25        void updateNode(int l, int r, int i) {
26            int mid = (l + r) / 2;
27            tree[i] = max({
28                (*arr)[mid] + (*arr)[mid + 1],
29                tree[i * 2],
30                tree[i * 2 + 1]
31            });
32        }
33
34        int query(int ql, int qr, int l, int r, int i) {
35            if (qr < l || r < ql)
36                return 0;
37
38            if (ql <= l && r <= qr)
39                return tree[i];
40
41            int mid = (l + r) / 2;
42
43            int ans = max(
44                query(ql, qr, l, mid, i * 2),
45                query(ql, qr, mid + 1, r, i * 2 + 1)
46            );
47
48            if (ql <= mid && mid + 1 <= qr)
49                ans = max(ans, (*arr)[mid] + (*arr)[mid + 1]);
50
51            return ans;
52        }
53
54        void add(int pos, int val, int l, int r, int i) {
55            if (pos < l || pos > r)
56                return;
57
58            if (l == r) {
59                (*arr)[pos] += val;
60                return;
61            }
62
63            int mid = (l + r) / 2;
64
65            add(pos, val, l, mid, i * 2);
66            add(pos, val, mid + 1, r, i * 2 + 1);
67
68            updateNode(l, r, i);
69        }
70    };
71
72    vector<int> maxActiveSectionsAfterTrade(string s, vector<vector<int>>& queries) {
73        int n = s.size();
74
75        int cnt = 0;
76        for (char c : s)
77            cnt += (c == '1');
78
79        vector<int> sep;
80        vector<int> sepx;
81
82        int last = 0;
83
84        for (int i = 1; i < n; i++) {
85            if (s[i] != s[i - 1]) {
86                if (s[last] == '0') {
87                    sep.push_back(i - last);
88                    sepx.push_back(last);
89                }
90                last = i;
91            }
92        }
93
94        if (s[last] == '0') {
95            sep.push_back(n - last);
96            sepx.push_back(last);
97        }
98
99        int m = sep.size();
100
101        vector<int> ans(queries.size(), cnt);
102
103        if (m == 0)
104            return ans;
105
106        SegTree seg(sep);
107
108        vector<int> nextZero(n, n);
109        vector<int> prevZero(n, -1);
110
111        for (int i = 1; i < n; i++) {
112            prevZero[i] = (s[i] == '0') ? i : prevZero[i - 1];
113        }
114
115        for (int i = n - 2; i >= 0; i--) {
116            nextZero[i] = (s[i] == '0') ? i : nextZero[i + 1];
117        }
118
119        for (int i = 0; i < queries.size(); i++) {
120            int l = queries[i][0];
121            int r = queries[i][1];
122
123            l = nextZero[l];
124            r = prevZero[r];
125
126            if (l > r)
127                continue;
128
129            int al = lower_bound(sepx.begin(), sepx.end(), l) - sepx.begin();
130
131            if (al == m || sepx[al] != l)
132                al--;
133
134            int ar = lower_bound(sepx.begin(), sepx.end(), r) - sepx.begin();
135
136            if (ar == m || sepx[ar] != r)
137                ar--;
138
139            int exl = l - sepx[al];
140            int exr = sep[ar] - r + sepx[ar] - 1;
141
142            seg.add(al, -exl, 0, m - 1, 1);
143            seg.add(ar, -exr, 0, m - 1, 1);
144
145            ans[i] = cnt + seg.query(al, ar, 0, m - 1, 1);
146
147            seg.add(al, exl, 0, m - 1, 1);
148            seg.add(ar, exr, 0, m - 1, 1);
149        }
150
151        return ans;
152    }
153};