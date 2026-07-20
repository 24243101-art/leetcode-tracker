// Last updated: 7/20/2026, 9:47:23 PM
1class Solution {
2public:
3    int maximumGap(vector<int>& nums) {
4        int n = nums.size();
5
6        if (n < 2)
7            return 0;
8
9        int minVal = *min_element(nums.begin(), nums.end());
10        int maxVal = *max_element(nums.begin(), nums.end());
11
12        if (minVal == maxVal)
13            return 0;
14
15        int bucketSize = max(1, (maxVal - minVal) / (n - 1));
16        int bucketCount = (maxVal - minVal) / bucketSize + 1;
17
18        vector<int> bucketMin(bucketCount, INT_MAX);
19        vector<int> bucketMax(bucketCount, INT_MIN);
20        vector<bool> used(bucketCount, false);
21
22        for (int num : nums) {
23            int idx = (num - minVal) / bucketSize;
24
25            bucketMin[idx] = min(bucketMin[idx], num);
26            bucketMax[idx] = max(bucketMax[idx], num);
27            used[idx] = true;
28        }
29
30        int prevMax = minVal;
31        int ans = 0;
32
33        for (int i = 0; i < bucketCount; i++) {
34            if (!used[i])
35                continue;
36
37            ans = max(ans, bucketMin[i] - prevMax);
38            prevMax = bucketMax[i];
39        }
40
41        return ans;
42    }
43};