"""
23. Merge k Sorted Lists

Share
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

## solution1: similar to merge sort algorithm, the time complexity is O(nklogn)
# n is the length of lists; k is the length of each list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def helper(self, lists, left, right):
        if left < right:
            mid = left + (right - left) // 2
            return self.merge(self.helper(lists, left, mid), self.helper(lists, mid + 1, right))
        return lists[left]

    def merge(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        dummy = ListNode(-1)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
                cur = cur.next
                cur.next = None
            else:
                cur.next = l2
                l2 = l2.next
                cur = cur.next
                cur.next = None
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        left = 0
        right = len(lists) - 1
        return self.helper(lists, left, right)


# solution2: maintain a heap with length of n, n is the length of lists, k is the length of each list
# time complexity is O(nklogn), the time of updating heap is logn
# python heapq, if the item is a tuple, it includes three elements, the first is the priority and compared item, we use it to compare;
# the second is count item, each count item is different from all of others; the third is task object
import heapq

class Solution:

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        stack = []
        heapq.heapify(stack)
        order = 0
        for l in lists:
            if l:
                heapq.heappush(stack, (l.val, order, l))
                order += 1

        res = ListNode(-1)
        dummy = res

        while stack:
            cur = heapq.heappop(stack)[2]
            res.next = cur
            res = res.next
            if cur.next:
                heapq.heappush(stack, (cur.next.val, order, cur.next))
                res.next = None
                order += 1

        return dummy.next