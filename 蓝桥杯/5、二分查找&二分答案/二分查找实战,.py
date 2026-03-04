#2563 统计公平数对的数目 力扣


#与顺序无关，先排序
#lower-x <=y <= upper-x
#即对一个x，区间[i+1,n)中有多少个数出现在 区间[lower-x,upper-x]
#即求 L = bisect(a, [lower]-x-1)  R = bisect(a, upper-x)-1
#答案为R-L+1

"""
from bisect import *
class Solution:
    def countFairPairs(self, a: List[int], lower: int, upper: int) -> int:
        a.sort()
        res = 0
        for i in range(len(a)):
            L = bisect(a, lower - x - 1, i+1)
            R = bisect(a, upper - x, i+1) - 1
            res += R - L + 1
        return res
        
"""