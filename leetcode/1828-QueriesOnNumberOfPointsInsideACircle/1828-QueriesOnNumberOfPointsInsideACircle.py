# Last updated: 9/6/2026, 2:55:26 PM
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = []
        for query in queries:
            x_j, y_j, r_j = query
            count = 0
            for point in points:
                x_i, y_i = point
                del_x = x_j - x_i
                del_y = y_j - y_i
                if (del_x**2 + del_y**2) <= r_j**2:
                    count += 1
            answer.append(count)
        
        return answer