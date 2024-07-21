arr=list(int(input()) for _ in range(7))

s=[]
for a in arr:
    if a%2==1:
        s.append(a)

if len(s)==0:
    print(-1)
else:
    print(sum(s))
    print(min(s))