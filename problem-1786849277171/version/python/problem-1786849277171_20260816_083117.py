# Last updated: 8/16/2026, 8:31:17 AM
1class Solution:
2    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
3        tx, ty = target
4        min_dist = float('inf')
5        best_index = -1
6        for i, (dx, dy, d_range) in enumerate(drones):
7            manhattan_dist = abs(dx - tx) + abs(dy - ty)
8            if manhattan_dist <= d_range and manhattan_dist < min_dist:
9                min_dist = manhattan_dist
10                best_index = i
11        return best_index
12                    