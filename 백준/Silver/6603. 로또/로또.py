from itertools import combinations

while 1:
    arr=list(map(int,input().split()))

    n=arr[0]
    if n==0:
        break
    arr2=arr[1::]
    
    combi=list(combinations(arr2,6))
    
    for c in combi:
        print(*c)
    print()