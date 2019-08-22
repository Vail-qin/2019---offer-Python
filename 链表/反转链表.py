#输入一个链表，反转链表后，输出新链表的表头。

'''思路：首先初始化两个指针，pre保存当前节点的上一个节点，tmp暂存当前节点的下一个节点
          '''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None:
            return None
        pre = None
        nex = None
        while(pHead!=None):
            nex = pHead.next
            pHead.next = pre
            pre = pHead
            pHead = nex
        return pre

