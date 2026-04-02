n=int(input())#전체 사람 수
a,b=map(int,input().split())#촌수 계산해야하는 서로 다른 두 사람 번호
m=int(input())#부모 자식들 관계 개수

parent=[0]*(n+1)
for _ in range(m):
    x,y=map(int,input().split())
    parent[y]=x

d1=dict()
cur=a
cnt=0
while cur!=0:
    d1[cur]=cnt
    cur=parent[cur]
    cnt+=1
# print(d1)
d2=dict()
cur=b
cnt=0
while cur!=0:
    if cur in d1:
        # print(d2)
        print(d1[cur]+cnt)
        exit(0)
    d2[cur]=cnt
    cur=parent[cur]
    cnt+=1
# print(d2)
print(-1)

# 9
# 2 7
# 7
# 1 2
# 1 3
# 2 7
# 2 8
# 2 9
# 4 5
# 4 6