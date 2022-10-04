class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cost_per_day = [0 for i in range(days[-1]+1)]
        
        for i in range(1, len(cost_per_day)):
            if i not in days:
                cost_per_day[i] = cost_per_day[i-1]
            else:
                cost_per_day[i] = min(cost_per_day[max(0, i-1)]+costs[0],
                                      cost_per_day[max(0, i-7)]+costs[1],
                                      cost_per_day[max(0, i-30)]+costs[2])
        print(cost_per_day)
        return cost_per_day[-1]
        
        
        