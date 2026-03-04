# 2226. 每个小孩最多能分到多少糖果 力扣

class Solution:
    def maximumCandies(self, a: List[int], k: int) -> int:
        if sum(a) <k: return 0
        lo, hi = 1, max(a) + 1
        def check(res):
            return sum(x // res for x in a) < k
        while lo < hi:
            i = (lo + hi) >> 1
            if check(i): hi = i
            else: lo = i + 1
        return lo - 1
