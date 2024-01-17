t=int(input())
for _ in range(t):
    arr=list(input())
    # print(arr)
    cnt=0
    if arr[0]==')':
        print('NO')
        continue
    while arr:
        p=arr.pop(0)
        # print(p)
        if p=='(':
            cnt+=1
        else:
            cnt-=1
        if cnt<0:
            break
    if cnt==0:
        print('YES')
    else:
        print("NO")