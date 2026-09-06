# Last updated: 9/6/2026, 2:55:29 PM
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # Prefix-suffix approach to have O(n) time complexity
        n = len(boxes)
        answer = [0] * n
        i = 0

        # Total number of balls from left to right
        left_count = int(boxes[0])

        # Number of moves taken moving from left to right
        left_moves = 0

        # Left to right pass 
        for i in range(1, n):
            # When you move 1 to the right, depending on
            # current total num of balls, you have to move
            # each ball to the right
            left_moves += left_count

            # Store this result into the current answer 
            answer[i] = left_moves

            # Update total number of balls based on current index
            left_count += int(boxes[i])

        # Total number of balls from right to left
        right_count = int(boxes[-1])

        # Total number of movements going right to left
        right_moves = 0

        # Right to left pass
        for i in range(n - 2, -1, -1):
            right_moves += right_count

            # You should add this to the existing number of moves
            answer[i] += right_moves

            right_count += int(boxes[i])

        return answer
