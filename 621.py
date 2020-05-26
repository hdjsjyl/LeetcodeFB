"""
621. Task Scheduler
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
"""

# Solution: time complexity: O(n), memeory complexity: O(n)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dicts = {}
        maxes = 0
        for task in tasks:
            dicts[task] = dicts.get(task, 0) + 1
            if dicts[task] > maxes:
                maxes = dicts[task]

        cnt = 0
        cnt2 = 0
        sums = 0
        for key, value in dicts.items():
            sums += value
            if value > maxes - 1:
                cnt += maxes - 1
                cnt2 += value - maxes + 1
            else:
                cnt += value

        cnt -= maxes - 1
        if cnt >= (maxes - 1) * (n):
            return sums
        else:
            return (maxes - 1) * (n + 1) + cnt2