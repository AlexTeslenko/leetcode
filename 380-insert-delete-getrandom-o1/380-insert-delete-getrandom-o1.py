import random
class RandomizedSet:

    def __init__(self):
        self.elements = []
        self.el_to_idx = {}
        

    def insert(self, val: int) -> bool:
        if val in self.el_to_idx:
            return False
        
        self.elements.append(val)
        self.el_to_idx[val] = len(self.elements) - 1
        return True
        

    def remove(self, val: int) -> bool:
        if not val in self.el_to_idx:
            return False

        idx = self.el_to_idx[val]
        last_el = self.elements[-1]
        self.elements[idx] = last_el
        self.el_to_idx[last_el] = idx
        
        self.elements.pop()
        del self.el_to_idx[val]
        
        return True
        

    def getRandom(self) -> int:
        return choice(self.elements)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()