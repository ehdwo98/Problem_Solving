cnt=0
while 1:
    cnt+=1
    l,p,v=map(int,input().split())
    if l==0 and p==0 and v==0:
        break
    if v%p<l:
        ans=(v//p)*l+(v%p)
    else:
        ans=(v//p)*l+l
    print(f"Case {cnt}: {ans}")