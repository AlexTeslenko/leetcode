from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent_to_children = {}
        num_components = 0
        visited_nodes = [False for i in range(n)]
        
        for pr, child in edges:
            if pr not in parent_to_children:
                parent_to_children[pr] = []
            if child not in parent_to_children:
                parent_to_children[child] = []
            
            parent_to_children[child].append(pr)
            parent_to_children[pr].append(child)


        for pr in range(n):
            queue = deque([pr])
            if not visited_nodes[pr]:
                num_components += 1
                while queue:
                    node = queue.popleft()
                    visited_nodes[node] = True
                    if node in parent_to_children:
                        for child in parent_to_children[node]:
                            if not visited_nodes[child]:
                                queue.append(child)
        
        return num_components
                    
                
        
        
            
            
        
        
        
        
        
        
        
        
        
        
        
        '''

        visited_nodes = [False for i in range(n)]
        num_components = 0
        
        def visit_component(comp, edges):
            if visited_nodes[comp] or not len(edges):
                return
            
            if comp == edges[0][0]:
                visited_nodes[comp] = True
                print(edges)
                print(visited_nodes)
                visit_component(edges[0][1], edges[1:])
             
            
        #visit_component(edges[0][0], edges[0:])
        for i, edge in enumerate(edges):
            if not visited_nodes[edge[0]]:
                #print(edge[0])
                num_components += 1
                visit_component(edge[0], edges[i:])
        
        return num_components
        '''
        
        
        
            
                
                
            
        