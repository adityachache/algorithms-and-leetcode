class Solution:
    def climbStairs(self, n: int) -> int:
            
        def memoized(n, memo={}):
            
            if n in memo:
                return memo[n]
            
            if n <= 1:
                return 1

            memo[n] = memoized(n-1) + memoized(n-2)
           
            return memo[n]
            
        return memoized(n)