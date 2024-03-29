
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        buildings = []
        cur_max_building = -1
        
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > cur_max_building:
                cur_max_building = heights[i]
                buildings.append(i)
        
        buildings.reverse()
        
        return buildings
            