import sys
input=sys.stdin.readline

n=int(input())

arr=list(map(int,input().split()))

ans=0
def recur(sum):
    global ans
    if len(arr)==2:
        ans=max(sum,ans)
        return
    for i in range(1,len(arr)-1):
        tmp=arr.pop(i)
        recur(sum+arr[i-1]*arr[i])
        arr.insert(i,tmp)

recur(0)
print(ans)