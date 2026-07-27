# Last updated: 7/27/2026, 7:07:13 PM
1from threading import Semaphore
2
3class ZeroEvenOdd:
4    def __init__(self, n):
5        self.n = n
6        self.zeroSem = Semaphore(1)
7        self.evenSem = Semaphore(0)
8        self.oddSem = Semaphore(0)
9
10    def zero(self, printNumber):
11        for i in range(1, self.n + 1):
12            self.zeroSem.acquire()
13            printNumber(0)
14            if i % 2 == 1:
15                self.oddSem.release()
16            else:
17                self.evenSem.release()
18
19    def even(self, printNumber):
20        for i in range(2, self.n + 1, 2):
21            self.evenSem.acquire()
22            printNumber(i)
23            self.zeroSem.release()
24
25    def odd(self, printNumber):
26        for i in range(1, self.n + 1, 2):
27            self.oddSem.acquire()
28            printNumber(i)
29            self.zeroSem.release()