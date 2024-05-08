n,s=map(int,input().split())
arr=list(map(int,input().split()))

ans=0
def func(k,hap):
    global ans
    if k>=n:
        return
    hap+=arr[k]
    if hap==s:
        ans+=1
    func(k+1,hap)
    func(k+1,hap-arr[k])

func(0,0)
print(ans)