import sys
input=sys.stdin.readline

n,m=map(int,input().split())

dic=dict()

for _ in range(n):
    arr=input().split()
    t=int(arr[0])
    s=arr[1]
    r=''.join(arr[2:2+3])
    if r in dic.keys():
        dic[r].append(s)
    else:
        dic[r]=list()
        dic[r].append(s)
        
for _ in range(m):
    r=''.join(input().split())
    if r not in dic.keys():
        print("!")
    elif len(dic[r])==1:
        print(*dic[r])
    else:
        print("?")