# Last updated: 7/9/2026, 10:07:17 AM
from collections import defaultdict

class Solution:
    def getLength(self, nums):
        dremovical = nums[:]

        n = len(nums)
        ans = 1

        for l in range(n):
            freq = defaultdict(int)
            cnt_freq = defaultdict(int)

            max_freq = 0
            distinct = 0
            active_freqs = 0

            for r in range(l, n):
                x = nums[r]

                old_f = freq[x]
                new_f = old_f + 1
                freq[x] = new_f

                if old_f == 0:
                    distinct += 1
                else:
                    cnt_freq[old_f] -= 1
                    if cnt_freq[old_f] == 0:
                        del cnt_freq[old_f]
                        active_freqs -= 1

                if cnt_freq[new_f] == 0:
                    active_freqs += 1
                cnt_freq[new_f] += 1

                max_freq = max(max_freq, new_f)

                ok = False

                if distinct == 1:
                    ok = True
                elif (
                    max_freq % 2 == 0
                    and active_freqs == 2
                    and max_freq in cnt_freq
                    and max_freq // 2 in cnt_freq
                ):
                    ok = True

                if ok:
                    ans = max(ans, r - l + 1)

        return ans