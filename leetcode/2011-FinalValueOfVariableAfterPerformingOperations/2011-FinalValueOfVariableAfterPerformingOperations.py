# Last updated: 9/6/2026, 2:55:23 PM
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0

        for operation in operations:
            if operation == "--X" or operation == "X--":
                result -= 1
            elif operation == "++X" or operation == "X++":
                result += 1
        return result