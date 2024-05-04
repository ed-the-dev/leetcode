from typing import List
from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        students_queue: deque = deque(students)

        sandos_pntr: int = 0

        # Count from when

        sando_last_taken: int = 0

        while (len(students_queue) > 0):

            if sando_last_taken >= len(students_queue):
                return len(students_queue)

            next_student: int = students_queue.popleft()
            if next_student == sandwiches[sandos_pntr]:
                sandos_pntr += 1
                sando_last_taken = 0
            
            else:
                students_queue.append(next_student)
                sando_last_taken += 1

        return 0





