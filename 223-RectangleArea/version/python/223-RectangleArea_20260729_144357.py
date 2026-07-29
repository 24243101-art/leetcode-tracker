# Last updated: 7/29/2026, 2:43:57 PM
1class Solution:
2    def computeArea(self, ax1, ay1, ax2, ay2,
3                    bx1, by1, bx2, by2):
4
5        area1 = (ax2 - ax1) * (ay2 - ay1)
6        area2 = (bx2 - bx1) * (by2 - by1)
7
8        overlapWidth = max(0, min(ax2, bx2) - max(ax1, bx1))
9        overlapHeight = max(0, min(ay2, by2) - max(ay1, by1))
10
11        overlap = overlapWidth * overlapHeight
12
13        return area1 + area2 - overlap