from collections import deque
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        output = deque([])
        closest_num = math.inf
        closest_idx = -1
        for i in range(len(arr)):
            if abs(arr[i] - x) < abs(closest_num - x):
                closest_num = arr[i]
                closest_idx = i
        
        output.append(closest_num)
        
        left_ptr, right_ptr = closest_idx - 1, closest_idx + 1
        
        while len(output) < k:
            #print(left_ptr, right_ptr)
            if left_ptr >= 0 and right_ptr < len(arr):
                if abs(arr[left_ptr] - x) < abs(arr[right_ptr] - x):
                    output.appendleft(arr[left_ptr])
                    left_ptr -= 1
                elif abs(arr[left_ptr] - x) == abs(arr[right_ptr] - x):
                    if arr[left_ptr] < arr[right_ptr]:
                        output.appendleft(arr[left_ptr])
                        left_ptr -= 1
                    else:
                        output.append(arr[right_ptr])
                        right_ptr += 1
                else:
                    output.append(arr[right_ptr])
                    right_ptr += 1
            elif left_ptr < 0 and right_ptr < len(arr):
                output.append(arr[right_ptr])
                right_ptr += 1
            elif right_ptr >= len(arr):
                output.appendleft(arr[left_ptr])
                left_ptr -= 1
            #print(output)
        
        return list(output)