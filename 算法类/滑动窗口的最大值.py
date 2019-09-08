# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        res = []
        if size == 0 or size > len(num):
            return res
        for i in range(len(num) - size + 1):
            tmp = []
            for j in range(i, i + size):
                tmp.append(num[j])
            res.append(max(tmp))
        return res
