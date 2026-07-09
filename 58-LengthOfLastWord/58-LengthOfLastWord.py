# Last updated: 7/9/2026, 10:10:41 AM
class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        words = s.split(" ")
        return len(words[-1])
