class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for s in operations:
            if stack:
                if s == "+":
                    addition = int(stack[-1]) + int(stack[-2])
                    stack.append(addition)
                elif s == "D":
                    double = 2 * int(stack[-1])
                    stack.append(double)
                elif s == "C":
                    stack.pop()
                else:
                    stack.append(int(s))
            else:
                stack.append(int(s))
        
        return sum(stack)