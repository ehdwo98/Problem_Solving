k=int(input())

arr=[]
for _ in range(k):
    p=int(input())
    if p==0:
        arr.pop()
    else:
        arr.append(p)

print(sum(arr))