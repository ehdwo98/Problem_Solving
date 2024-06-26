n=int(input())

arr=[]
def func(n):
    i=2
    while i<=n:
        if n%i==0:
            arr.append(i)
            n//=i
        else:
            i+=1

func(n)
for a in arr:
    print(a)