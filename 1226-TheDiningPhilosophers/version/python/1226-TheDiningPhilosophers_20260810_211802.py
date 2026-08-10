# Last updated: 8/10/2026, 9:18:02 PM
1from threading import Lock
2
3class DiningPhilosophers:
4
5    def __init__(self):
6        self.lock = Lock()
7
8    def wantsToEat(self, philosopher, pickLeftFork, pickRightFork,
9                   eat, putLeftFork, putRightFork):
10
11        with self.lock:
12            pickLeftFork()
13            pickRightFork()
14
15            eat()
16
17            putLeftFork()
18            putRightFork()