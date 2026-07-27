// Last updated: 7/27/2026, 10:35:06 AM
1class Solution {
2    public String shortestPalindrome(String s) {
3
4        if (s == null || s.length() <= 1) {
5            return s;
6        }
7
8        String t = new StringBuilder(s).reverse().toString();
9
10        for (int i = 0; i < t.length(); i++) {
11
12            if (s.startsWith(t.substring(i))) {
13
14                return t.substring(0, i) + s;
15            }
16        }
17
18        return t + s;
19    }
20}