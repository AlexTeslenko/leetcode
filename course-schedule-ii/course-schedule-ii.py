from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_map = {}
        num_parents = {}
        courses = []
        
        for prereq in prerequisites:
            child, parent = prereq
            if parent not in adj_map:
                adj_map[parent] = []
            
            adj_map[parent].append(child)
        
        queue = deque([])
            
        for prereq in prerequisites:
            child, parent = prereq
            if child not in num_parents:
                num_parents[child] = 0
            
            num_parents[child] += 1
        
        for i in range(numCourses):
            if i not in num_parents:
                queue.append(i)
        
        while queue:
            cur_node = queue.popleft()
            courses.append(cur_node)
            
            if cur_node in adj_map:
                for child in adj_map[cur_node]:
                    num_parents[child] -= 1
                    if num_parents[child] == 0:
                        queue.append(child)
                
        
        return courses if len(courses) == numCourses else []
                
        
                
        