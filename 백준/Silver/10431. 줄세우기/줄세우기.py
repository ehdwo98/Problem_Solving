import sys
input=sys.stdin.readline

p=int(input())

arr=list(list(map(int,input().split())) for _ in range(p))

for a in arr:
    ans=0
    for i in range(2,len(a)):
        for j in range(1,i):
            if a[i]<a[j]:
                tmp=a[i]
                a[j+1:i+1]=a[j:i]
                a[j]=tmp
                ans+=i-j
                break
    print(a[0],ans)