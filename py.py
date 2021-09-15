class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return len(arr)
        res = 1
        cur = 1
        for i in range(1, len(arr)-1):
            if cur>1:
                if  (gt and arr[i] > arr[i+1]) or ((not gt) and arr[i] < arr[i+1]):
                    cur += 1
                    gt=not gt
                elif arr[i]==arr[i+1]:
                    res=max(res, cur)
                    cur=1
                else:
                    res=max(res, cur)
                    cur=2
                    gt=arr[i]<arr[i+1]
            elif arr[i]!=arr[i-1]:
                cur=2
                gt=arr[i]<arr[i+1]
        return max(res, cur)
