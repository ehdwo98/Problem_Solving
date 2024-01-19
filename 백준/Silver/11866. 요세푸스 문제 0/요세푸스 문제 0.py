from sys import stdin
input=stdin.readline

n,k=map(int,input().split())

arr=[x+1 for x in range(n)]

res=[]
while arr:
    for i in range(k-1):
        arr.append(arr.pop(0))
    res.append(arr.pop(0))
    
print('<',end='')
print(', '.join(map(str,res)),end='')
print('>')