class Solution:
    def isValid(self, s: str) -> bool:
        solution = 'stack'

        if solution == 'stack':
            stack = []
            close_to_open_map = {
                ')' : '(',
                ']' : '[',
                '}' : '{'
            }

            for char in s:
                if char in close_to_open_map:
                    if stack and stack[-1] == close_to_open_map[char]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(char)

            return not stack

        if solution == 'brute':
            while '()' in s or '[]' in s or '{}' in s:
                s = s.replace('()', '')
                s = s.replace('[]', '')
                s = s.replace('{}', '')

            return s == ''