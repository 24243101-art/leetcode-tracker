// Last updated: 7/20/2026, 9:52:44 PM
1class Solution {
2public:
3    int rob(vector<int>& nums) {
4        int n = nums.size();
5
6        if (n == 1)
7            return nums[0];
8
9        vector<int> dp(n);
10
11        dp[0] = nums[0];
12        dp[1] = max(nums[0], nums[1]);
13
14        for (int i = 2; i < n; i++) {
15            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i]);
16        }
17
18        return dp[n - 1];
19    }
20};