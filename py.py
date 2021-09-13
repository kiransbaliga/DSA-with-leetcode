class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b=text.count('b')
        a=text.count('a')
        l=text.count('l')
        o=text.count('o')
        n=text.count('n')
        l=l//2
        o=o//2  
        y=min(b,a,l,o,n)
        return y
        