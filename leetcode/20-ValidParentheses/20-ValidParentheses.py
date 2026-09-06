# Last updated: 9/6/2026, 2:56:35 PM
class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            ')' : '(',
            ']' : '[',
            '}' : "{"
        }

        stack = []

        for bracket in s:
            if bracket in map:
                if stack and stack[-1] == map[bracket]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(bracket)
        
        return not stack