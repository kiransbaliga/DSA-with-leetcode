class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        n=len(s)
        i=0
        j=n-1
        while i<j:
            while i<n and not s[i].isalpha():
                i+=1
            while j>=0 and not s[j].isalpha():
                j-=1
            if i<j:
                s=s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:]
            i+=1
            j-=1
        return s