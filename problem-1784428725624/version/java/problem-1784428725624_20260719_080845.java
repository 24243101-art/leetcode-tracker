// Last updated: 7/19/2026, 8:08:45 AM
1class Solution {
2    public boolean canReach(int[] start, int[] target) {
3        int startParity = (start[0] + start[1]) % 2;
4        int targetParity = (target[0] + target[1]) % 2;
5        if (startParity < 0) startParity += 2;
6        if (targetParity < 0) targetParity += 2;
7        return startParity == targetParity;
8    }
9}