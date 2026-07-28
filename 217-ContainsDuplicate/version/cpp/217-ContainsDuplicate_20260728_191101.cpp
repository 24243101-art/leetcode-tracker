// Last updated: 7/28/2026, 7:11:01 PM
1class Solution {
2public:
3    bool containsNearbyDuplicate(vector<int>& nums, int k) {
4        unordered_map<int, int> mp;
5
6        for (int i = 0; i < nums.size(); i++) {
7            if (mp.count(nums[i]) && i - mp[nums[i]] <= k)
8                return true;
9
10            mp[nums[i]] = i;
11        }
12
13        return false;
14    }
15};