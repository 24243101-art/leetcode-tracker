# Last updated: 7/9/2026, 10:10:59 AM
class Solution(object):
    def groupAnagrams(self, strs):
        from collections import defaultdict
        groups = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            groups[key].append(word)

        return list(groups.values())

        