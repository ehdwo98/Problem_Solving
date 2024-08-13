import sys
input=sys.stdin.readline

n=int(input())

arr=list(list(map(int,input().split())) for _ in range(n))
arr.sort()

ans=0
l_end=(3,1)
for i in range(n):
    sm,sd,em,ed=arr[i]
    if (sm,sd)<=l_end<(em,ed):
        max_end=(em,ed)
        while i+1<n:
            nsm,nsd,nem,ned=arr[i+1]
            if l_end>=(nsm,nsd) and max_end<(nem,ned):
                max_end=(nem,ned)
            i+=1
        ans+=1
        l_end=max_end

        if (11,30)<l_end:
            print(ans)
            exit(0)
print(0)