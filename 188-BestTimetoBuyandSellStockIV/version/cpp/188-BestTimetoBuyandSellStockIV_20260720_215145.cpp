// Last updated: 7/20/2026, 9:51:45 PM
1class Solution {
2public:
3    int maxProfit(int k, vector<int>& prices) {
4        int n = prices.size();
5
6        if (n == 0 || k == 0)
7            return 0;
8
9        if (k >= n / 2) {
10            int profit = 0;
11            for (int i = 1; i < n; i++) {
12                if (prices[i] > prices[i - 1])
13                    profit += prices[i] - prices[i - 1];
14            }
15            return profit;
16        }
17
18        vector<vector<int>> dp(k + 1, vector<int>(n, 0));
19
20        for (int t = 1; t <= k; t++) {
21            int maxDiff = -prices[0];
22
23            for (int i = 1; i < n; i++) {
24                dp[t][i] = max(dp[t][i - 1], prices[i] + maxDiff);
25                maxDiff = max(maxDiff, dp[t - 1][i] - prices[i]);
26            }
27        }
28
29        return dp[k][n - 1];
30    }
31};