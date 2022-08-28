class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ids_total_time = {i:0 for i in range(n)}
        stack = []
        i = 0
        while i < len(logs):
            cur_log = logs[i].split(':')
            cur_idx = int(cur_log[0])
            op = cur_log[1]
            cur_time = int(cur_log[2])

            if op == 'start':
                stack.append([cur_idx, op, cur_time])
            else:
                prev_log = stack.pop()
                total_time = cur_time - prev_log[2] + 1
                ids_total_time[cur_idx] += total_time
                
                if stack:
                    ids_total_time[stack[-1][0]] -= total_time
            
            i += 1
            
        return list(ids_total_time.values())
                

        