class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        intersected_array = []
        
        i = 0
        for num in nums1:
            
            while i < len(nums2) and num >= nums2[i]:
                print(num)
                print(nums2[i])
                if num == nums2[i]:
                    if num not in intersected_array:
                        intersected_array.append(num)
                    break
                else:
                    i += 1
        return intersected_array
        