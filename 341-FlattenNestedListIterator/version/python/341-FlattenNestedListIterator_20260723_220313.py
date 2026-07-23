# Last updated: 7/23/2026, 10:03:13 PM
1class NestedIterator(object):
2
3    def __init__(self, nestedList):
4        self.data = []
5        self.index = 0
6
7        def flatten(lst):
8            for item in lst:
9                if item.isInteger():
10                    self.data.append(item.getInteger())
11                else:
12                    flatten(item.getList())
13
14        flatten(nestedList)
15
16    def next(self):
17        value = self.data[self.index]
18        self.index += 1
19        return value
20
21    def hasNext(self):
22        return self.index < len(self.data)