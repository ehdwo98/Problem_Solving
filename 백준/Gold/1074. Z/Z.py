N,r,c=map(int,input().split())

def cal(N,r,c,):
    if N==0:
        return 0
    return 2*(r%2)+(c%2)+4*cal(N-1,r//2,c//2)

print(cal(N,r,c))