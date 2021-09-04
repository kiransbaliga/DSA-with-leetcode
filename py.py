def median(nums,k):
    nums.sort()
    if k%2==0:
        return(nums[(k//2)-1])
    else:
        return(nums[k//2])        

def subseq(arr,idx,subaarr,lst,k):
    
    if idx == len(arr):
        if len(subaarr)==k:
            lst.append(subaarr)
    else:
        subseq(arr,idx+1,subaarr,lst,k)
        subseq(arr,idx+1,subaarr+[arr[idx]],lst,k)
    
t=int(input())
for _ in range(t):
    lst=[]
    ans=[]
    res=-1
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    subseq(a,0,[],lst,k)
    for i in lst:
        cpy=i
        tmp=median(i,k)
        if tmp>res:
            res=tmp
            ans=cpy
    print(res)
    print(*ans)

                