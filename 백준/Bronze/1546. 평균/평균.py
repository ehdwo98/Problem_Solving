n=int(input())
score=list(map(int,input().split()))
m=max(score)
#print(m,score)

def cal(i):
    return i/m*100

score=map(cal,score)
print(sum(score)/n)