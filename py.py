class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        joball=sorted(list(zip(startTime, endTime, profit)))
        st=[i[0]  for i in joball]
        n=len(joball)
        dp=[0] * (n+1)
        for k in range(n-1,-1,-1):
            temp=bisect_left(st,joball[k][1])
            dp[k]=max(joball[k][2] + dp[temp], dp[k+1])
        return dp[0]
        