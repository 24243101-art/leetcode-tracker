# Last updated: 7/9/2026, 10:12:17 AM
class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False 
        return str(x) == str(x)[::-1]  

        