# Last updated: 9/6/2026, 2:55:13 PM
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n - 1):
            # Reset n_copy to test next base
            n_copy = n
            # Clear the result list containing digits
            result = []
            while n_copy != 0:
                result.append(n_copy % i)
                n_copy //= i
                print(result)
            if result[::-1] != result:
                return False
        return True
            