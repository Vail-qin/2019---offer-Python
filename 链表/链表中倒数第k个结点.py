'''思想：设置p1,p2快慢指针，快指针p1先走k-1步，之后快慢指针同时前进，
快指针p1走到链表最后一个结点时，慢指针p2刚好指向倒数第k个结点
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head == None or k <= 0:
            return None
        p1 = head
        p2 = head
        while k > 1:
            if p1.next != None:
                p1 = p1.next
                k -= 1
            else:
                return None
        while p1.next != None:
            p1 = p1.next
            p2 = p2.next
        return p2

