# Last updated: 7/23/2026, 10:01:32 PM
1class PeekingIterator:
2    def __init__(self, iterator):
3        self.iterator = iterator
4        self.nextElement = None
5
6        if self.iterator.hasNext():
7            self.nextElement = self.iterator.next()
8
9    def peek(self):
10        return self.nextElement
11
12    def next(self):
13        current = self.nextElement
14
15        if self.iterator.hasNext():
16            self.nextElement = self.iterator.next()
17        else:
18            self.nextElement = None
19
20        return current
21
22    def hasNext(self):
23        return self.nextElement is not None