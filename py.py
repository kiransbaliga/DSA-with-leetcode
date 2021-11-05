class Solution:
    def arrangeCoins(self, n: int) -> int:
        lvl=0
        i=1
        while n>=0:
            n=n-i
            i+=1
            lvl+=1
        return lvl-1