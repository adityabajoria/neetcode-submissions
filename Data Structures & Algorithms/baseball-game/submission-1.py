class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for s in operations:
            if s == '+':
                stack.append(int(stack[-1] + int(stack[-2])))
            elif s == 'D':
                stack.append(2 * int(stack[-1]))
            elif s == 'C':
                stack.pop()
            else:
                stack.append(int(s))
        
        return sum(stack)