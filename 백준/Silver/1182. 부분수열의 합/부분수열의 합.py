from itertools import combinations

n,s=map(int,input().split())
arr=list(map(int,input().split()))

ans=0
hap=[]
def func(k):
    global ans
    if k>n:
        return
    combi=list(combinations(arr,k))
    for c in combi:
        if sum(c)==s:
            ans+=1
    else:
        func(k+1)

func(1)
print(ans)