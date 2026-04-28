class Solution:
    def isValid(self, s: str) -> bool:
        brackets_dict = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []

        for bracket in s:
            # Opening bracket
            if bracket in brackets_dict.values():
                stack.append(bracket)
            # Closing bracket
            else:
                if not stack or stack[-1] != brackets_dict[bracket]:
                    return False
                stack.pop()

        return not stack