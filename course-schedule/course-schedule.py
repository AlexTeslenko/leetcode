from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {}
        num_parents = {}
        
        for pair in prerequisites:
            if pair[1] not in adj_list:
                adj_list[pair[1]] = []
            adj_list[pair[1]].append(pair[0])
            
            if pair[0] not in num_parents:
                num_parents[pair[0]] = 0
            num_parents[pair[0]] += 1
        
        queue = deque([])
        for i in range(numCourses):
            if i not in num_parents:
                queue.append(i)
        
        course_order = []

        while queue:
            parent = queue.popleft()
            course_order.append(parent)
            if parent in adj_list:
                childs = adj_list[parent]
            
                for child in childs:
                    num_parents[child] -= 1
                
                    if num_parents[child] == 0:
                        queue.append(child)
            
        if len(course_order) != numCourses:
            return False
        
        return True
                
        
        