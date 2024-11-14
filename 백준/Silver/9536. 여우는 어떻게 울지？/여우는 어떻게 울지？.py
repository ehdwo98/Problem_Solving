import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    dic=dict()
    arr=list(input().rstrip().split())
    while 1:
        tmp=input().rstrip()
        if tmp=='what does the fox say?':
            break
        res=list(tmp.split())[2]
        dic[res]=0
    # print(dic)
    ans=[]
    for a in arr:
        if a not in dic:
            ans.append(a)
    print(*ans)