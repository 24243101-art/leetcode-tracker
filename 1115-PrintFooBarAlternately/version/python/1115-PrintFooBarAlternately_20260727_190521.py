# Last updated: 7/27/2026, 7:05:21 PM
1from threading import Semaphore
2
3class FooBar:
4    def __init__(self, n):
5        self.n = n
6        self.fooSem = Semaphore(1)
7        self.barSem = Semaphore(0)
8
9    def foo(self, printFoo):
10        for i in range(self.n):
11            self.fooSem.acquire()
12
13            printFoo()
14
15            self.barSem.release()
16
17    def bar(self, printBar):
18        for i in range(self.n):
19            self.barSem.acquire()
20
21            printBar()
22
23            self.fooSem.release()