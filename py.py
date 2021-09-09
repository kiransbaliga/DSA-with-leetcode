class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        m=len(mines)

        if m==n*n: return 0
        
        vis=set()
        
        for i,j in mines:
            vis.add((i,j))   # mark all Zeroes
        ans=1

        # left, right , up , down...
        lurd=[[[0,0,0,0] for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            for j in range(n):

                if (i,j) not in vis:
                     # check left and up from 0-n
        
                    lurd[i][j][0]=(lurd[i][j-1][0]+1) if j-1>=0 else 1   
                    lurd[i][j][1]=(lurd[i-1][j][1]+1) if i-1>=0 else 1
        
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):

                if (i,j) not in vis:
                         # check right and down from n-1 to 0 
                    lurd[i][j][2]=(lurd[i][j+1][2]+1) if j+1<n else 1
                    lurd[i][j][3]=(lurd[i+1][j][3]+1) if i+1<n else 1

                ans=max(ans,min(lurd[i][j]))
        return ans