class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opened = {'(': ')', '{': '}', '[': ']'}
        for c in s:
            if c in opened:
                stack.append(c)
            else:
                if stack and opened[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        return True if not stack else False