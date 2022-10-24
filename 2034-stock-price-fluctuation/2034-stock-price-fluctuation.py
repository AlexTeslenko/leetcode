from sortedcontainers import SortedDict
class StockPrice:

    def __init__(self):
        self.time_to_price = {}
        self.price_to_freq = SortedDict()
        self.latest = None

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.time_to_price:
            old_price = self.time_to_price[timestamp]
            self.price_to_freq[old_price] -= 1
            
            if self.price_to_freq[old_price] == 0:
                del self.price_to_freq[old_price]
        
        self.time_to_price[timestamp] = price
        
        if price not in self.price_to_freq:
            self.price_to_freq[price] = 0
        self.price_to_freq[price]  += 1
        
        if self.latest:
            if self.latest[0] <= timestamp:
                self.latest[0] = timestamp
                self.latest[1] = price
        else:
            self.latest = [timestamp, price]
        

    def current(self) -> int:
        return self.latest[1]

    def maximum(self) -> int:
        return self.price_to_freq.keys()[-1]

    def minimum(self) -> int:
        return self.price_to_freq.keys()[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()