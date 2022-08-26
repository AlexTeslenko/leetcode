class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        list1_ptr, list2_ptr = 0, 0
        merged_lists = []
        while list1_ptr < len(firstList) and list2_ptr < len(secondList):
            if firstList[list1_ptr][1] < secondList[list2_ptr][0]:
                list1_ptr += 1
            elif firstList[list1_ptr][0] <= secondList[list2_ptr][0] and \
                firstList[list1_ptr][1] >= secondList[list2_ptr][0]:
                second_part = min(firstList[list1_ptr][1], secondList[list2_ptr][1])
                merged_lists.append([secondList[list2_ptr][0], second_part])
                if second_part == secondList[list2_ptr][1]:
                    list2_ptr += 1
                if second_part == firstList[list1_ptr][1]:
                    list1_ptr += 1
            elif secondList[list2_ptr][0] <= firstList[list1_ptr][0] and \
                secondList[list2_ptr][1] >= firstList[list1_ptr][0]:
                second_part = min(firstList[list1_ptr][1], secondList[list2_ptr][1])
                merged_lists.append([firstList[list1_ptr][0], second_part])
                if second_part == secondList[list2_ptr][1]:
                    list2_ptr += 1
                if second_part == firstList[list1_ptr][1]:
                    list1_ptr += 1
                
            elif secondList[list2_ptr][1] < firstList[list1_ptr][0]:
                list2_ptr += 1
                
                
        return merged_lists
            
        