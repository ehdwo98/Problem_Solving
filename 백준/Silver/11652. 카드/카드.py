import sys

input=sys.stdin.readline
n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))
arr.sort()#오름차순이여야 공동 1위일때도 작은 수가 출력됨

cnt,max_cnt=0,0
max_val=0
tmp=arr[0]
for a in arr:
    if a==tmp:
        cnt+=1
    else:
        if cnt>max_cnt:
            max_cnt=cnt
            max_val=tmp
        cnt=1
        tmp=a

if cnt>max_cnt:
    max_val=arr[n-1]

print(max_val)