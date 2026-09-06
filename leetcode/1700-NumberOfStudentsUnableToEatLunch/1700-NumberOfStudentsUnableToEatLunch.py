# Last updated: 9/6/2026, 2:55:32 PM
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while sandwiches and sandwiches[0] in students:
            if students[0] != sandwiches[0]:
                temp = students[0]
                students.pop(0)
                students.append(temp)
            else:
                students.pop(0)
                sandwiches.pop(0)
        
        return len(sandwiches)