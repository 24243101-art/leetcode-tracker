// Last updated: 7/20/2026, 9:54:48 PM
1class Solution {
2public:
3    int maximalSquare(vector<vector<char>>& matrix) {
4        int m = matrix.size();
5        int n = matrix[0].size();
6
7        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
8        int maxSide = 0;
9
10        for (int i = 1; i <= m; i++) {
11            for (int j = 1; j <= n; j++) {
12                if (matrix[i - 1][j - 1] == '1') {
13                    dp[i][j] = 1 + min({dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]});
14                    maxSide = max(maxSide, dp[i][j]);
15                }
16            }
17        }
18
19        return maxSide * maxSide;
20    }
21};