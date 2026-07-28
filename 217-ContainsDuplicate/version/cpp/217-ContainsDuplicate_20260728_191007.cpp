// Last updated: 7/28/2026, 7:10:07 PM
1class Solution {
2public:
3    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
4        vector<pair<int, int>> events;
5
6        for (auto &b : buildings) {
7            events.push_back({b[0], -b[2]});
8            events.push_back({b[1], b[2]});
9        }
10
11        sort(events.begin(), events.end());
12
13        multiset<int> heights;
14        heights.insert(0);
15
16        unordered_map<int, vector<int>> endMap;
17        for (auto &b : buildings) {
18            endMap[b[1]].push_back(b[2]);
19        }
20
21        int i = 0, n = events.size();
22        int prev = 0;
23        vector<vector<int>> ans;
24
25        while (i < n) {
26            int x = events[i].first;
27
28            while (i < n && events[i].first == x && events[i].second < 0) {
29                heights.insert(-events[i].second);
30                i++;
31            }
32
33            if (endMap.count(x)) {
34                for (int h : endMap[x]) {
35                    heights.erase(heights.find(h));
36                }
37            }
38
39            while (i < n && events[i].first == x && events[i].second > 0) {
40                i++;
41            }
42
43            int curr = *heights.rbegin();
44
45            if (curr != prev) {
46                ans.push_back({x, curr});
47                prev = curr;
48            }
49        }
50
51        return ans;
52    }
53};