from collections import Counter

arr=map(int,input().split())

C=list(Counter(arr).items())
C.sort(key=lambda x:(-x[1],-x[0]))
if len(C)==1:
    print(10000+C[0][0]*1000)
elif len(C)==2:
    print(1000+C[0][0]*100)
else:
    print(C[0][0]*100)