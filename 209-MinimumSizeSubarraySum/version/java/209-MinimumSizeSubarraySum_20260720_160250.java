// Last updated: 7/20/2026, 4:02:50 PM
1import java.util.TreeSet;
2
3class Solution {
4    public boolean containsNearbyAlmostDuplicate(int[] nums, int indexDiff, int valueDiff) {
5
6        TreeSet<Long> set = new TreeSet<>();
7
8        for (int i = 0; i < nums.length; i++) {
9
10            Long candidate = set.ceiling((long) nums[i] - valueDiff);
11
12            if (candidate != null && candidate <= (long) nums[i] + valueDiff) {
13                return true;
14            }
15
16            set.add((long) nums[i]);
17
18            if (i >= indexDiff) {
19                set.remove((long) nums[i - indexDiff]);
20            }
21        }
22
23        return false;
24    }
25}