// Last updated: 7/22/2026, 9:57:56 PM
1class Solution {
2public:
3    int maxActiveSectionsAfterTrade(string s) {
4        int n = (int)s.size();
5
6        vector<int> zeroes;
7
8        int oneCount = 0;
9
10        for (int i = 0, cnt = 0; i < n; i++) {
11            if (s[i] == '0') {
12                cnt++;
13            }
14            else {
15                oneCount++;
16            }
17
18            if (cnt != 0 && (s[i] == '1' || i == n - 1)) {
19                zeroes.push_back(cnt);
20                cnt = 0;
21            }
22        }
23
24        int maxScore = 0;
25
26        for (int i = 1; i < (int)zeroes.size(); i++) {
27            maxScore = max(maxScore, zeroes[i] + zeroes[i - 1]);
28        }
29
30        return oneCount + maxScore;
31    }
32};