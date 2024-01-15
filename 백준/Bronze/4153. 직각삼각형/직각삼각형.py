while 1 :
    a,b,c=map(int,input().split())
    if a==0 and b==0 and c==0:
        break
    else:
        arr=[]
        arr.append(a)
        arr.append(b)
        arr.append(c)
        arr.sort()
        # print(arr)
        if arr[0]*arr[0]+arr[1]*arr[1]==arr[2]*arr[2]:
            print("right")
        else:
            print("wrong")