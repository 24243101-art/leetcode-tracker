# Last updated: 8/21/2026, 9:20:02 PM
1class MyStack:
2
3    def __init__(self):
4        self.q1 = []
5        self.q2 = []
6
7    def push(self, x: int) -> None:
8        self.q2.append(x)
9
10        while self.q1:
11            self.q2.append(self.q1.pop(0))
12
13        self.q1, self.q2 = self.q2, self.q1
14
15    def pop(self) -> int:
16        return self.q1.pop(0)
17
18    def top(self) -> int:
19        return self.q1[0]
20
21    def empty(self) -> bool:
22        return len(self.q1) == 0