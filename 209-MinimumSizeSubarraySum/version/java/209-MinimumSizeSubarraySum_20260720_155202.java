// Last updated: 7/20/2026, 3:52:02 PM
1class Solution {
2    public int minSubArrayLen(int target, int[] nums) {
3
4        int left = 0;
5        int sum = 0;
6        int minLength = Integer.MAX_VALUE;
7
8        for (int right = 0; right < nums.length; right++) {
9            sum += nums[right];
10
11            while (sum >= target) {
12                minLength = Math.min(minLength, right - left + 1);
13                sum -= nums[left];
14                left++;
15            }
16        }
17
18        return (minLength == Integer.MAX_VALUE) ? 0 : minLength;
19    }
20}