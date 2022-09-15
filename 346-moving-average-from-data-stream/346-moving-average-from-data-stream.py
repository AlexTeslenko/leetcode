from collections import deque
class MovingAverage:
    
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.window_sum = 0
        

    def next(self, val: int) -> float:
        self.window_sum += val
        self.queue.append(val)
        if len(self.queue) > self.size:
            tail = self.queue.popleft()
            self.window_sum -= tail
        
        return self.window_sum / len(self.queue)
    
    '''
    def __init__(self, size: int):
        self.window_size = size
        self.nums = deque()
        
    def next(self, val: int) -> float:
        self.nums.append(val)
        if len(self.nums) > self.window_size:
            self.nums.popleft()
        
        return sum(self.nums) / self.window_size if len(self.nums) == self.window_size else sum(self.nums) / len(self.nums)
    '''



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)