# Last updated: 7/27/2026, 2:59:06 PM
1import heapq
2
3class Solution:
4    def findKthLargest(self, nums, k):
5        heap = []
6
7        for num in nums:
8            heapq.heappush(heap, num)
9
10            if len(heap) > k:
11                heapq.heappop(heap)
12
13        return heap[0]