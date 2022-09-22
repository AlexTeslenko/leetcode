class Solution:
    def defangIPaddr(self, address: str) -> str:
        ip_list = address.split('.')
        return '[.]'.join(ip_list)
        