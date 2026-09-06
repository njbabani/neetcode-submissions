# Last updated: 9/6/2026, 2:56:39 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # If x is negative, it cannot be a palidrome
        if x < 0:
            return False

        # Store the reverse integer
        x_inv = 0
        # This will be divided by 10 to get each digit
        x_temp = x

        while x_temp != 0:
            # Modulo for this gives the rightmost digit
            digit = x_temp % 10

            # Shift everything up by 10 then add in the new RHS digit
            x_inv = x_inv * 10 + digit

            # Divide by 10 and floor it to get the next left digits
            x_temp //= 10

        return x_inv == x