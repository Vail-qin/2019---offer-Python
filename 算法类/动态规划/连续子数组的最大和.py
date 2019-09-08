'''思想：记录一个临时值和一个最终值，初始化为第一个数，然后循环数组
如果临时值大于0，则加上当前循环的值，如果小于0，则设置临时值为当前循环的值
然后比较最终值和临时值的大小'''

# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        res = array[0]
        temp = array[0]
        for i in range(1, len(array)):
            if(temp>0):
                temp += array[i]
            else:
                temp = array[i]
            if res<temp:
                res = temp
        return res

'''法二：dp[i]表示以元素array[i]结尾的最大连续子数组和.
以[-2,-3,4,-1,-2,1,5,-3]为例，可以发现,
dp[0] = -2，dp[1] = -3，dp[2] = 4，dp[3] = 3
以此类推,会发现
dp[i] = max{dp[i-1]+array[i],array[i]}.
'''
# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        n = len(array)
        dp = [i for i in array]
        for i in range(1,n):
            dp[i] = max(dp[i-1]+array[i],array[i])
        return max(dp)