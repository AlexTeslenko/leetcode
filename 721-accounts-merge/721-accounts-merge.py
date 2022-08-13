class Solution:
    
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj_list = {}
        visited = set()
        
        for account in accounts:
            first_email = account[1]
            if first_email not in adj_list:
                adj_list[first_email] = []
            for i in range(2, len(account)):
                cur_email = account[i]
                adj_list[first_email].append(cur_email)
                if cur_email not in adj_list:
                    adj_list[cur_email] = []
                adj_list[cur_email].append(first_email)
        
        
        merged_accounts = []
        for acc in accounts:
            merged_account = []
            self.dfs(merged_account, acc[1], adj_list, visited)
            if len(merged_account):
                merged_account.sort()
                merged_account.insert(0, acc[0])

                merged_accounts.append(merged_account)
        
        return merged_accounts
        
        
    
    def dfs(self, merged_acocunt, email, adj_list, visited):
        if email not in visited:
            visited.add(email)
            merged_acocunt.append(email)
            
            for neighbour in adj_list[email]:
                self.dfs(merged_acocunt, neighbour, adj_list, visited)
            
                
        