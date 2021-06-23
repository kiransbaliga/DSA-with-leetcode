
def solve():
    
    n=int(input())
    lst=list(map(int,input().split()))
    s=sum(lst)
    if (s==n):
        print("0")
    elif(s<=0):
        print("1")
    elif (s>0):
        print(s-n)
        
def main():
    t=int(input())
    while(t>=0):
            solve() 
            t-+1 
main()