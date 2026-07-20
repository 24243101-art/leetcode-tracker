// Last updated: 7/20/2026, 3:57:38 PM
1import java.util.HashMap;
2
3class Solution {
4    public boolean containsNearbyDuplicate(int[] nums, int k) {
5
6        HashMap<Integer, Integer> map = new HashMap<>();
7
8        for (int i = 0; i < nums.length; i++) {
9
10            if (map.containsKey(nums[i])) {
11                if (i - map.get(nums[i]) <= k) {
12                    return true;
13                }
14            }
15
16            map.put(nums[i], i);
17        }
18
19        return false;
20    }
21}