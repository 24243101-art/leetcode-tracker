// Last updated: 7/26/2026, 7:54:57 PM
1class Solution {
2    public int countPrimes(int n) {
3        if (n <= 2) return 0;
4
5        boolean[] isPrime = new boolean[n];
6
7        for (int i = 2; i < n; i++) {
8            isPrime[i] = true;
9        }
10
11        for (int i = 2; i * i < n; i++) {
12            if (isPrime[i]) {
13                for (int j = i * i; j < n; j += i) {
14                    isPrime[j] = false;
15                }
16            }
17        }
18
19        int count = 0;
20        for (int i = 2; i < n; i++) {
21            if (isPrime[i]) {
22                count++;
23            }
24        }
25
26        return count;
27    }
28}