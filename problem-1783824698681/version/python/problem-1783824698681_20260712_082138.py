# Last updated: 7/12/2026, 8:21:38 AM
1from datetime import datetime
2class Solution(object):
3    def secondsBetweenTimes(self, startTime, endTime):
4        fmt = "%H:%M:%S"
5        t1 = datetime.strptime(startTime, fmt)
6        t2 = datetime.strptime(endTime, fmt)
7        return int(abs(t2 - t1).total_seconds())
8        