# Last updated: 9/6/2026, 2:56:06 PM
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_count = Counter(ransomNote)
        m_count = Counter(magazine)

        for char in r_count:
            if r_count[char] > m_count.get(char, 0):
                return False
        
        return True