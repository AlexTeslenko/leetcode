class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if ':' not in queryIP and '.' not in queryIP:
            return "Neither"
        if ':' in queryIP:
            ip_parts = queryIP.split(':')
            if len(ip_parts) != 8:
                return "Neither"
            for ip_part in ip_parts:
                if len(ip_part) < 1 or len(ip_part) > 4:
                    return "Neither"
                for ch in ip_part:
                    if not ch.isalnum():
                        return "Neither"
                    if ch.isalpha():
                        if ch not in 'ABCDEFabcdef':
                            return "Neither"    
            
            return "IPv6"
        if '.' in queryIP:
            ip_parts = queryIP.split('.')
            if len(ip_parts) != 4:
                return "Neither"
            for ip_part in ip_parts:
                if not ip_part.isnumeric():
                    return "Neither" 
                if len(ip_part) > 1 and int(ip_part[0]) == 0:
                    return "Neither"
                if int(ip_part) < 0 or int(ip_part) > 255:
                    return "Neither"

            
            return "IPv4"