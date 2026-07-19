// Last updated: 7/19/2026, 8:57:52 AM
1import java.util.*;
2import java.util.HashSet;
3class Solution {
4    public int minimumGroups(String[] words) {
5        Set<String> uniqueGroups = new HashSet<>();
6        for (String w : words){
7            int n = w.length();
8            char[] evenArr = new char[(n + 1) / 2];
9            char[] oddArr = new char[n / 2];
10            int e = 0, o = 0;
11            for (int i = 0; i < n; i++){
12                if (i % 2 == 0) evenArr[e++] = w.charAt(i);
13                else oddArr[o++] = w.charAt(i);
14            }
15            String canonicalEven = getMinRotation(new String(evenArr));
16            String canonicalOdd = getMinRotation(new String(oddArr));
17            uniqueGroups.add(canonicalEven + "#" + canonicalOdd);
18        }
19        return uniqueGroups.size();
20    }
21    private String getMinRotation(String s){
22        int n = s.length();
23        if (n <= 1) return s;
24        int i  = 0, j = 1, k = 0;
25        while (i < n && j < n && k < n){
26            char c1 = s.charAt((i + k) % n);
27            char c2 = s.charAt((j + k) % n);
28            if (c1 == c2){
29                k++;
30            } else {
31                if (c1 > c2) i += k + 1;
32                else j += k + 1;
33                if (i == j) j++;
34                k = 0;
35            }
36        }
37        int start = Math.min(i, j);
38        return s.substring(start) + s.substring(0, start);
39    }
40}