# Last updated: 7/27/2026, 10:15:23 AM
1from collections import deque
2
3class Solution:
4    def canFinish(self, numCourses, prerequisites):
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
18        count = 0
19
20        while queue:
21            node = queue.popleft()
22            count += 1
23
24            for neighbor in graph[node]:
25                indegree[neighbor] -= 1
26
27                if indegree[neighbor] == 0:
28                    queue.append(neighbor)
29
30        return count == numCourses