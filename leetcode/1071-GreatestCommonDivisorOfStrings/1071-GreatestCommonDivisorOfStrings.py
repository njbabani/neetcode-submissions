# Last updated: 9/6/2026, 2:55:51 PM
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        # If doesn't work for smaller string then don't care
        len_min = min(len1, len2)

        for l in range(len_min, 0, -1):
            if len1 % l != 0 or len2 % l != 0:
                continue

            candidate = str1[:l]

            factor1, factor2 = len1 // l, len2 // l

            if candidate * factor1 == str1 and candidate * factor2 == str2:
                return candidate

        return ""