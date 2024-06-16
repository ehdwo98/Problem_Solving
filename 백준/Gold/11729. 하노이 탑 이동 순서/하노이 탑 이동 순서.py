n=int(input())

cnt=0
arr=[]
def hanoi(n,s,t,e):
    global cnt
    if n==1:
        arr.append([s,e])
        cnt+=1
        return
    else:
        hanoi(n-1,s,e,t)
        arr.append([s,e])
        cnt+=1
        hanoi(n-1,t,s,e)

hanoi(n,1,2,3)
print(cnt)
for a in arr:
    print(*a)