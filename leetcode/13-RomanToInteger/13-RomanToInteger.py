# Last updated: 9/6/2026, 2:56:37 PM
class Solution:
    def romanToInt(self, s: str) -> int:
        # Create a hash map for roman numerials
        r_map = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        '''
        The pattern is that if the current string interation is less than the next,
        then you can perform a subtraction based on current string idx value else
        just add this to the total sum
        '''

        # We will add and subtract then abs this value to get correct int
        result = 0

        for i in range(len(s) - 1):
            if r_map[s[i]] < r_map[s[i + 1]]:
                result -= r_map[s[i]]
            else:
                result += r_map[s[i]]

        result += r_map[s[-1]]
        return result
