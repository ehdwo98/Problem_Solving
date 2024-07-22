from collections import Counter

for _ in range(3):
    arr=map(int,input().split())
    C=Counter(arr)
    n=C[0]
    if n==0:
        print('E')
    elif n==1:
        print('A')
    elif n==2:
        print('B')
    elif n==3:
        print('C')
    else:
        print('D')