while 1:
    arr=list(input())
    arr=list("".join(arr))
    #print(arr)
    arr2=[]
    if arr==['.']:
        break
    c=1
    for a in arr:
        if a=='(':
            arr2.append(a)
        elif a=='[':
            arr2.append(a)
        elif a==')':
            if len(arr2)==0:
                c=0
                break
            p=arr2.pop()
            if p!='(':
                c=0
                break
        elif a==']':
            if len(arr2)==0:
                c=0
                break
            p=arr2.pop()
            if p!='[':
                c=0
                break

    if len(arr2)==0 and c:
        print('yes')
    else:
        print('no')