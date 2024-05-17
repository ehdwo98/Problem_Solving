from itertools import combinations

while 1:
    arr=list(map(int,input().split()))

    n=arr[0]
    if n==0:
        break
    arr2=arr[1::]

    arr3=[]
    isused=[0]*n

    def lotto(idx):
        if len(arr3)==6:
            print(*arr3)
            return
        for i in range(idx,len(arr2)):
            if isused[i]==0:
                arr3.append(arr2[i])
                isused[i]=1
                lotto(i+1)
                isused[i]=0
                arr3.pop()
    
    lotto(0)
    print()