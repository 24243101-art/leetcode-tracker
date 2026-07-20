// Last updated: 7/20/2026, 3:50:50 PM
1import java.util.*;
2
3class Solution {
4    public List<String> findRepeatedDnaSequences(String s) {
5
6        Set<String> seen = new HashSet<>();
7        Set<String> repeated = new HashSet<>();
8
9        for (int i = 0; i <= s.length() - 10; i++) {
10            String dna = s.substring(i, i + 10);
11
12            if (!seen.add(dna)) {
13                repeated.add(dna);
14            }
15        }
16
17        return new ArrayList<>(repeated);
18    }
19}