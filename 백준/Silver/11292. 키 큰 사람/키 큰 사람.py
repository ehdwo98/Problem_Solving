import sys
input=sys.stdin.readline

while 1:
    n=int(input())
    if n==0:
        break
    dic=dict()
    for _ in range(n):
        s,h=input().split()
        if h not in dic:
            dic[h]=list()
            dic[h].append(s)
        else:
            dic[h].append(s)
    # print(dic)
    arr=sorted(dic.items(),key=lambda x:-float(x[0]))
    print(*arr[0][1])
