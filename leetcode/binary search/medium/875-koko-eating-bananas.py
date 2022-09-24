class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # we have to find k and k can be any number starting 1 (because eating speed cannot start from 0) upto the max from the pile
            
        minInt = float('inf')

        low = 1
        high = max(piles)

        # we can use binary search to find the minimum k by dividing each pile by the k value to get the hours taken to eat that pile
        while low <= high:

            k = (low+high)//2

            hoursTaken = 0
            for i in piles:
                hoursTaken += math.ceil(i/k)

            if hoursTaken <= h:
                minInt = min(minInt, k)
                high = k - 1
            else:
                low = k + 1

        return minInt