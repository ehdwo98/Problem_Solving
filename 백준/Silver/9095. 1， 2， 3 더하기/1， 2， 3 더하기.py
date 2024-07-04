T=int(input())

def dp(x):
    if x>n:
        return
    if x>3:
        arr[x]+=1
    dp(x+1)
    dp(x+2)
    dp(x+3)

for _ in range(T):
    n=int(input())
    arr=[0]*11
    arr[1]=1
    arr[2]=2
    arr[3]=4
    dp(0)
    print(arr[n])