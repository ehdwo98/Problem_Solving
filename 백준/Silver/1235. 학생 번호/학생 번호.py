import sys
input=sys.stdin.readline

n=int(input())
arr=list(list(input().rstrip()) for _ in range(n))


for i in range(100):
    tmp=dict()
    for j in range(n):
        res=''.join(arr[j][::-1][:i])
        tmp[res]=1
    # print(tmp)
    if len(tmp)==n:
        print(i)
        break
