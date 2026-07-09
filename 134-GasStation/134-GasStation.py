# Last updated: 7/9/2026, 10:08:06 AM
class Solution:
    def canCompleteCircuit(self, gas, cost):
        total_tank = 0
        curr_tank = 0
        start = 0

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]

            if curr_tank < 0:
                start = i + 1
                curr_tank = 0

        return start if total_tank >= 0 else -1
