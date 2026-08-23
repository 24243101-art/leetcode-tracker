# Last updated: 8/23/2026, 1:07:46 PM
1class MyQueue:
2
3    def __init__(self):
4        self.stack1 = []
5        self.stack2 = []
6
7    def push(self, x: int) -> None:
8        self.stack1.append(x)
9
10    def pop(self) -> int:
11        self.move()
12        return self.stack2.pop()
13
14    def peek(self) -> int:
15        self.move()
16        return self.stack2[-1]
17
18    def empty(self) -> bool:
19        return not self.stack1 and not self.stack2
20
21    def move(self):
22        if not self.stack2:
23            while self.stack1:
24                self.stack2.append(self.stack1.pop())