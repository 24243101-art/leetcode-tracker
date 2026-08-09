# Last updated: 8/9/2026, 8:09:36 AM
1class Solution:
2    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
3        prices.sort(reverse=True)
4        discounts.sort(reverse=True)
5        total_price = 0.0
6        for i in range(len(prices)):
7            if i < len(discounts):
8                p = prices[i]
9                d = discounts[i]
10                total_price += (p * (100 - d)) / 100.0
11            else:
12                total_price += prices[i]
13        return total_price