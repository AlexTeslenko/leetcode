class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        output = []
        for el in arr1:
            if el in arr2 and el in arr3:
                output.append(el)
        
        return output