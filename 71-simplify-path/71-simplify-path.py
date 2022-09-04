from collections import deque
class Solution:
    def simplifyPath(self, path: str) -> str:
        queue = deque()
        path_els = path.split('/')
        print(path_els)
        for el in path_els:
            if el == '..':
                if queue:
                    queue.pop()
            elif el not in ['', '.']:
                queue.append(el)
           
        return '/' + '/'.join(queue)
    
        