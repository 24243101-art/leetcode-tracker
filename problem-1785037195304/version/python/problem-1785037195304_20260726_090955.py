# Last updated: 7/26/2026, 9:09:55 AM
1import heapq
2class Solution(object):
3    def minCost(self, m, n, penalty):
4        R = len(penalty)
5        C = len(penalty[0]) if R > 0 else 0
6        start_cost = 1
7        pq = [(start_cost, 0, 0, 1)]
8        dist = [[[float('inf')] * 2 for _ in range(C)] for _ in range(R)]
9        dist[0][0][1] = start_cost
10        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
11        while pq:
12            cost, r, c, is_odd = heapq.heappop(pq)
13            if r == R - 1 and c == C - 1:
14                return cost
15            if cost > dist[r][c][is_odd]:
16                continue
17            next_parity = 1 - is_odd
18            p_val = penalty[r][c]
19            for i, (dr, dc) in enumerate(dirs):
20                nr, nc = r + dr, c + dc
21                if 0 <= nr < R and 0 <= nc < C:
22                    is_valid_dir = (is_odd == 1 and i < 2) or (is_odd == 0 and i >= 2)
23                    move_cost = (nr + 1) * (nc + 1)
24                    if not is_valid_dir:
25                        move_cost += p_val
26                    next_cost = cost + move_cost
27                    if next_cost < dist[nr][nc][next_parity]:
28                        dist[nr][nc][next_parity] = next_cost
29                        heapq.heappush(pq, (next_cost, nr, nc, next_parity))
30            wait_cost = cost + p_val
31            if wait_cost < dist[r][c][next_parity]:
32                dist[r][c][next_parity] = wait_cost
33                heapq.heappush(pq, (wait_cost, r, c, next_parity))
34        return -1