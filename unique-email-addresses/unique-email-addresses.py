class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        
        for email in emails:
            name, domain_name = email.split('@')

            filtered_name = ''
            for ch in name:
                if ch == '.':
                    continue
                elif ch == '+':
                    break
                filtered_name = filtered_name + ch
            
            unique_emails.add((filtered_name, domain_name))
        
                
        return len(unique_emails)
        