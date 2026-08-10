# Last updated: 8/10/2026, 9:10:01 PM
1from threading import Condition
2
3class FizzBuzz:
4    def __init__(self, n):
5        self.n = n
6        self.current = 1
7        self.condition = Condition()
8
9    def fizz(self, printFizz):
10        while True:
11            with self.condition:
12                while self.current <= self.n and not (
13                    self.current % 3 == 0 and self.current % 5 != 0
14                ):
15                    self.condition.wait()
16
17                if self.current > self.n:
18                    self.condition.notify_all()
19                    return
20
21                printFizz()
22                self.current += 1
23                self.condition.notify_all()
24
25    def buzz(self, printBuzz):
26        while True:
27            with self.condition:
28                while self.current <= self.n and not (
29                    self.current % 5 == 0 and self.current % 3 != 0
30                ):
31                    self.condition.wait()
32
33                if self.current > self.n:
34                    self.condition.notify_all()
35                    return
36
37                printBuzz()
38                self.current += 1
39                self.condition.notify_all()
40
41    def fizzbuzz(self, printFizzBuzz):
42        while True:
43            with self.condition:
44                while self.current <= self.n and not (
45                    self.current % 3 == 0 and self.current % 5 == 0
46                ):
47                    self.condition.wait()
48
49                if self.current > self.n:
50                    self.condition.notify_all()
51                    return
52
53                printFizzBuzz()
54                self.current += 1
55                self.condition.notify_all()
56
57    def number(self, printNumber):
58        while True:
59            with self.condition:
60                while self.current <= self.n and (
61                    self.current % 3 == 0 or self.current % 5 == 0
62                ):
63                    self.condition.wait()
64
65                if self.current > self.n:
66                    self.condition.notify_all()
67                    return
68
69                printNumber(self.current)
70                self.current += 1
71                self.condition.notify_all()