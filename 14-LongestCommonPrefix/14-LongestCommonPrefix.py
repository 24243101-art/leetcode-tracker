# Last updated: 7/9/2026, 10:12:07 AM
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        # Iterate character by character using the first word as reference
        for i in range(len(strs[0])):
            char = strs[0][i]
            for s in strs[1:]:
                # Check index out of bounds or mismatch
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]
        
        return strs[0]
