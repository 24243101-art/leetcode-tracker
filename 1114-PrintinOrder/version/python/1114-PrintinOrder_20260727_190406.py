# Last updated: 7/27/2026, 7:04:06 PM
1from threading import Lock
2
3class Foo:
4    def __init__(self):
5        self.lock2 = Lock()
6        self.lock3 = Lock()
7
8        self.lock2.acquire()
9        self.lock3.acquire()
10
11    def first(self, printFirst):
12        printFirst()
13
14        self.lock2.release()
15
16    def second(self, printSecond):
17        self.lock2.acquire()
18
19        printSecond()
20
21        self.lock3.release()
22
23    def third(self, printThird):
24        self.lock3.acquire()
25
26        printThird()