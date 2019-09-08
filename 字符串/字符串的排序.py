#输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,
#则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

'思想：采用回溯递归法，循环遍历，每次固定一个字符，然后再选取剩下的字符进行递归'

# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if len(ss)<=1:
            return ss
        res = set()
        for i in range(len(ss)):
            for j in self.Permutation(ss[:i]+ss[i+1:]):
                res.add(ss[i]+j)
        return sorted(res)

if __name__ == '__main__':
    s = input()
    x = Solution()
    res = x.Permutation(s)
    print(res)