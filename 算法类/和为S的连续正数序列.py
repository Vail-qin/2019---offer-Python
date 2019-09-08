
'思想：采用滑动窗口的思想，设置双指针，初始值为1,2'
# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        res = []
        low = 1
        high = 2
        while low<high:
            cur = (low+high)*(high-low+1)/2
            if cur == tsum:
                tmp = []
                for i in range(low,high+1):
                    tmp.append(i)
                res.append(tmp)
                low +=1
            elif cur<tsum:
                high +=1
            else:
                low +=1
        return res