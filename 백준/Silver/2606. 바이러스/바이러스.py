comp=int(input())
pair=int(input())

list=[[] for _ in range(comp+1)]

for _ in range(pair):
    a,b=map(int,input().split())
    list[a].append(b)
    list[b].append(a)
    
#print(list)

flag=[0]*(comp+1)

cnt=0
def dfs(x):
    global cnt
    flag[x]=1
    for i in list[x]:
        if flag[i]==0:
            cnt+=1
            flag[i]=1
            dfs(i)
            
dfs(1)
print(cnt)