class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            # Counting char appearances creates
            # the alphabet signature key where
            # each list idx represents ordered
            # alphabet letter
            count = [0] * 26
            for c in s:
                # Shifts a ... z to be idx 0 till 25
                count[ord(c) - ord('a')] += 1

            # Dictionary keys must be immutable
            ans[tuple(count)].append(s)

        return list(ans.values())
            