// Last updated: 7/23/2026, 6:33:52 PM
1class Solution {
2public:
3    int uniqueXorTriplets(vector<int>& nums) {
4        int n = nums.size();
5        return n >= 3 ? 1 << (32 - __builtin_clz(n)) : n;
6    }
7};