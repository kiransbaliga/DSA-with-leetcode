class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        # the logic is to find the min of the options cause thats the part which is incremented the most times. 
        # We also have to check if ops contain anythong ass well.
        if not ops:return m*n
        a,b=m,n
        for i,j in ops:
            a=min(a,i)
            b=min(b,j)
        return a*b   