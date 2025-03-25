import sys
input=sys.stdin.readline

arr=map(int,input().split())

for a,b in zip(arr,[1,1,2,2,2,8]):
    print((b-a),end=' ')