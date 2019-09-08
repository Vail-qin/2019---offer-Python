#输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
# 要求不能创建任何新的结点，只能调整树中结点指针的指向。

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def convert(self, root):
        if root == None:
            return None
        #将左子树构造成双链表，并返回链表头节点
        leftNode = self.convert(root.left)
        p = leftNode
        # 定位至左子树双链表的最后一个节点
        while p and p.right:
            p = p.right
        #若左子树链表不为空，将当前root追加到左子树链表
        if leftNode:
            p.right = root
            root.left = p
        #将右子树构造成双链表，并返回链表头节点
        rightNode = self.convert(root.right)
        #如果右子树链表不为空，将该链表追加到root节点之后
        if rightNode:
            rightNode.left = root
            root.right = rightNode
        return leftNode if leftNode else root