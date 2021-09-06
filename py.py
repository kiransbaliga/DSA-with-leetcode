class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        finkey=keysPressed[0]
        fintime=releaseTimes[0]
        for i in range(1,len(releaseTimes)):
            reltime=releaseTimes[i]-releaseTimes[i-1]
            key=keysPressed[i]

            if reltime>fintime or (reltime==fintime and key>finkey):
                fintime=reltime 
                finkey=key  
        return finkey

