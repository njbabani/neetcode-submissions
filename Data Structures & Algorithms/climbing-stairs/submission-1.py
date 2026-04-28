class Solution:
    def climbStairs(self, n: int) -> int:
        solution = 'dp-td'

        if solution == 'recursion':
            def dfs(i):
                # When you have reached or exceeded step n
                if i >= n:
                    # 1 if you are at step n but 0 if exceeded
                    return i == n

                return dfs(i + 1) + dfs(i + 2)

            # Start at step 0
            return dfs(0)

        if solution == 'dp-td':
            cache = [-1] * n
            
            def dfs(i):
                # Base case
                if i >= n:
                    return i == n
                # In the event you have seen this case before
                if cache[i] != -1:
                    return cache[i]
                # If not, then compute this current step
                cache[i] = dfs(i + 1) + dfs(i + 2)
                return cache[i]

            return dfs(0)