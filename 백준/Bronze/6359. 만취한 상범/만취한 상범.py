def check(n):
    arr=[]
    for i in range(1,int(n**(1/2))+1):
        arr.append(i)
        if i**2!=n:
            arr.append(n//i)
    arr.sort()
    return len(arr)

T=int(input())

for _ in range(T):
    n=int(input())
    ans=0
    for i in range(1,n+1):
        cnt=check(i)
        if cnt%2==1:
            ans+=1
    print(ans)