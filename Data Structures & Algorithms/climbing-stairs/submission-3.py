class Solution:
    def climbStairs(self, n: int) -> int:
        solution = 'dp-so'

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

        if solution == 'dp-bu':
            # This base case is needed since it's a Fibonacci
            if n <= 2:
                return n
            # Fibonacci modified to match stairs solution
            dp = [0] * (n + 1)
            dp[0], dp[1] = 1, 1

            for i in range(2, n + 1):
                dp[i] = dp[i - 1] + dp[i - 2]

            return dp[i]

        if solution == 'dp-so':
            one, two = 1, 1

            for i in range(n - 1):
                temp = one
                one = one + two
                two = temp

            return one
