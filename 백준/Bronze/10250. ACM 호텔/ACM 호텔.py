T=int(input())
for _ in range(T):
    H,W,N=map(int,input().split())
    cnt=[]
    for w in range(1,W+1):
        for h in range(1,H+1):
            if w<10:
                ans=str(h)+str(0)+str(w)
            else:
                ans=str(h)+str(w)
            cnt.append(ans)
    print(cnt[N-1])