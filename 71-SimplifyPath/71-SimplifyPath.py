# Last updated: 7/9/2026, 10:10:16 AM
class Solution(object):
    def simplifyPath(self, path):
        parts = path.split('/')
        stack = []

        for part in parts:
            if part == '' or part == '.':
                continue
            elif part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return '/' + '/'.join(stack)
