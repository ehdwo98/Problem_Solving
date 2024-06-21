import sys
input=sys.stdin.readline

T=int(input())
while T:
    n,m=map(int,input().split())
    A=sorted(list(map(int,input().split())))
    B=sorted(list(map(int,input().split())))
    #print(A,B)
    cnt=0
    j=0
    for i in range(n):
        while 1:
            if j==m or A[i]<=B[j]:
                cnt+=j
                break
            else:
                j+=1
    print(cnt)
    T-=1