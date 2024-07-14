from itertools import combinations
arr=[]
for _ in range(9):
    arr.append(int(input()))

C=list(combinations(arr,7))
for c in C:
    if sum(c)==100:
        for i in sorted(c):
            print(i)
        break