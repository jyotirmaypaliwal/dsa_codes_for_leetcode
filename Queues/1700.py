# O(n^2) solution
# class Solution:
#     def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

#         while students:
#             if students[0] == sandwiches[0]:
#                 students.pop(0) 
#                 sandwiches.pop(0)

#             else:
#                 students.append(students[0])
#                 students.pop(0)
            
#             if not sandwiches or all(student != sandwiches[0] for student in students):
#                 break
#         return len(students)


