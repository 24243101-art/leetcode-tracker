// Last updated: 7/20/2026, 3:48:00 PM
1class Solution {
2    public int findPeakElement(int[] nums) {
3
4        int left = 0;
5        int right = nums.length - 1;
6
7        while (left < right) {
8            int mid = left + (right - left) / 2;
9
10            if (nums[mid] > nums[mid + 1]) {
11                right = mid;
12            } else {
13                left = mid + 1;
14            }
15        }
16
17        return left;
18    }
19}