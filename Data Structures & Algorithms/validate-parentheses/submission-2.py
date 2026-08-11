class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in closed:
                if stack and stack[-1] == closed[c]: # if opened char is stack top, pop it.
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c) # append non-closed characters
        if not stack:
            return True
        else:
            return False