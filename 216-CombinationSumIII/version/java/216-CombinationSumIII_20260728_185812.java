// Last updated: 7/28/2026, 6:58:12 PM
1class Solution {
2    public List<List<Integer>> combinationSum3(int k, int n) {
3        List<List<Integer>> result = new ArrayList<>();
4        backtrack(1, k, n, new ArrayList<>(), result);
5        return result;
6    }
7
8    private void backtrack(int start, int k, int target,
9                           List<Integer> current,
10                           List<List<Integer>> result) {
11
12        if (current.size() == k) {
13            if (target == 0) {
14                result.add(new ArrayList<>(current));
15            }
16            return;
17        }
18
19        for (int i = start; i <= 9; i++) {
20            if (i > target) {
21                break;
22            }
23
24            current.add(i);
25            backtrack(i + 1, k, target - i, current, result);
26            current.remove(current.size() - 1);
27        }
28    }
29}