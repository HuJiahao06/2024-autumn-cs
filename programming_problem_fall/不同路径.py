class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def roads(m,n):
            if m==1 or n==1:
                return 1
            else:
                return roads(m-1,n)+roads(m,n-1)
        return roads(m,n)