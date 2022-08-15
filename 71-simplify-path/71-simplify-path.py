from collections import deque
class Solution:
    def simplifyPath(self, path: str) -> str:
        path_splited = path.split('/')
        simplified_path = '/'
        
        queue = deque()
        for ch in path_splited:
            if ch == '..':
                if len(queue):
                    queue.pop()
            elif ch not in ['.', '']:
                queue.append(ch)
        
        while queue:
            ch = queue.popleft()
            simplified_path = simplified_path + ch + '/'
        
        if len(simplified_path) > 1:
            simplified_path = simplified_path[:-1]
        
        return simplified_path
            
        