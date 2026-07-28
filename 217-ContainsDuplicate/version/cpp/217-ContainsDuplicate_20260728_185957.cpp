// Last updated: 7/28/2026, 6:59:57 PM
1class Solution {
2public:
3    bool containsDuplicate(vector<int>& nums) {
4        unordered_set<int> s;
5
6        for (int num : nums) {
7            if (s.count(num))
8                return true;
9
10            s.insert(num);
11        }
12
13        return false;
14    }
15};