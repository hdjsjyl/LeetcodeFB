"""
636. Exclusive Time of Functions

On a single threaded CPU, we execute some functions.  Each function has a unique id between 0 and N-1.

We store logs in timestamp order that describe when a function is entered or exited.

Each log is a string with this format: "{function_id}:{"start" | "end"}:{timestamp}".  For example, "0:start:3" means the function with id 0 started at the beginning of timestamp 3.  "1:end:2" means the function with id 1 ended at the end of timestamp 2.

A function's exclusive time is the number of units of time spent in this function.  Note that this does not include any recursive calls to child functions.

The CPU is single threaded which means that only one function is being executed at a given time unit.

Return the exclusive time of each function, sorted by their function id.

"""

## time complexity: O(n)

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = {}
        for i in range(n):
            res[i] = 0
        prev = -1
        stack = []
        for log in logs:
            ss = log.strip().split(':')
            if ss[1] == 'start':
                flag = 0
            elif ss[1] == 'end':
                flag = 1
            ids = int(ss[0])
            time = int(ss[2])
            if not stack:
                stack.append([0, ids, time])
                prev = time
            else:
                if flag == 0 and stack[-1][0] == 0:
                    res[stack[-1][1]] += (time - prev)
                    stack.append([0, ids, time])
                    prev = time
                elif flag == 1 and stack[-1][0] == 0:
                    res[stack[-1][1]] += (time - prev)
                    stack.pop(0)
                    prev = time + 1
        re = []
        for i in range(n):
            re.append(res[i])

        return re



