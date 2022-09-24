class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
          
        # top floor == len(cost) which cost is 0 because if there is not staircase we are already on the top floor
        cost.append(0) 
        
        # we want to start iterating from the 3rd index from the end of the array
        for i in range(len(cost)-3, -1, -1):
            
            cost[i] += min(cost[i+1], cost[i+2])
            
        # return the minimun of first two values in array 
        return min(cost[0], cost[1])
            
          