// Last updated: 7/20/2026, 9:53:39 PM
1class Solution {
2    public int rob(int[] nums) {
3        int n = nums.length;
4
5        if (n == 1)
6            return nums[0];
7
8        return Math.max(robHouse(nums, 0, n - 2), robHouse(nums, 1, n - 1));
9    }
10
11    private int robHouse(int[] nums, int start, int end) {
12        int prev2 = 0;
13        int prev1 = 0;
14
15        for (int i = start; i <= end; i++) {
16            int curr = Math.max(prev1, prev2 + nums[i]);
17            prev2 = prev1;
18            prev1 = curr;
19        }
20
21        return prev1;
22    }
23}