class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict(list) means a regular dict but
        # if you access a key that doesn't exist,
        # it creates that key with an empty list
        # for that key value
        ans = defaultdict(list)
        
        for s in strs:
            sorted_s = ''.join(sorted(s))
            ans[sorted_s].append(s)

        return list(ans.values())