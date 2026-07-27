# Last updated: 7/27/2026, 10:18:04 AM
1from collections import deque
2
3class Solution:
4    def findOrder(self, numCourses, prerequisites):
5        graph = [[] for _ in range(numCourses)]
6        indegree = [0] * numCourses
7
8        for course, prereq in prerequisites:
9            graph[prereq].append(course)
10            indegree[course] += 1
11
12        queue = deque()
13
14        for i in range(numCourses):
15            if indegree[i] == 0:
16                queue.append(i)
17
18        order = []
19
20        while queue:
21            node = queue.popleft()
22            order.append(node)
23
24            for neighbor in graph[node]:
25                indegree[neighbor] -= 1
26
27                if indegree[neighbor] == 0:
28                    queue.append(neighbor)
29
30        if len(order) == numCourses:
31            return order
32
33        return []