# Last updated: 9/6/2026, 2:56:00 PM
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for operation in operations:
            if operation == '+' and len(stack) >= 2:
                stack.append(stack[-1] + stack[-2])
            elif operation == 'D' and len(stack) >= 1:
                stack.append(stack[-1] * 2)
            elif operation == 'C' and len(stack) >= 1:
                stack.pop()
            else:
                stack.append(int(operation))
            
        return sum(stack)