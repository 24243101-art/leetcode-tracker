// Last updated: 7/19/2026, 8:29:26 AM
1class Solution {
2    public boolean[] transformStr(String s, String[] strs) {
3        boolean[] ans = new boolean[strs.length];
4        int n = s.length(), sZeros = 0;
5        for(char c: s.toCharArray()) if (c == '0') sZeros++;
6        for (int k = 0; k < strs.length; k++){
7            String t = strs[k];
8            int tZeros = 0, tOnes = 0;
9            for (char c : t.toCharArray()){
10                if (c == '0') tZeros++;
11                if (c == '1') tOnes++;
12            }
13            if (tZeros > sZeros || tOnes > (n - sZeros)) continue;
14            int sPref = 0, tPref = 0, qPref = 0, qToZero = sZeros - tZeros;
15            ans[k] = true;
16            for (int i = 0; i < n; i++){
17                if (s.charAt(i) == '0') sPref++;
18                if (t.charAt(i) == '0') tPref++;
19                if (t.charAt(i) == '?') qPref++;
20                if ( tPref + Math.min(qPref, qToZero) < sPref){
21                    ans[k] = false;
22                    break;
23                }
24            }
25        }
26        return ans;
27    }
28}