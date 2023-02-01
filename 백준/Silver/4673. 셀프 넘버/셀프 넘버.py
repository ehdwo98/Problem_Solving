arr=[]
for i in range(1,10001,1):
    d=0
    d+=i
    n= list(map(int,str(i)))
    for j in range(len(n)):
        d+=n[j]
    arr.append(d)
    #print(arr)
    
for i in range(1,10001,1):
    if i not in arr:
        print(i)