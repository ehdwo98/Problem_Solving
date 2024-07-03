import sys,copy
input=sys.stdin.readline
n,m=map(int,input().split())

graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

tmp_graph=copy.deepcopy(graph)

D=[(1,0),(0,1),(-1,0),(0,-1)]

arr=[]
ans=0
for r in range(n):
    for c in range(m):
        if graph[r][c]!=6 and graph[r][c]!=0:
            arr.append([graph[r][c],r,c])
        if graph[r][c]==0:
            ans+=1

def move(r,c,d):
    d%=4
    while 1:
        r+=D[d][0]
        c+=D[d][1]
        if 0<=r<n and 0<=c<m and tmp_graph[r][c]!=6:
            if tmp_graph[r][c]==0:
                tmp_graph[r][c]='#'
        else:
            return


for i in range(4**len(arr)):
    case=i
    tmp_graph=copy.deepcopy(graph)
    for j in range(len(arr)):
        # print(case)
        case,d=divmod(case,4)
        # print(case,d)
        k,r,c=arr[j]
        if k==1:
            move(r,c,d)
        elif k==2:
            move(r,c,d);move(r,c,d+2)
        elif k==3:
            move(r,c,d);move(r,c,d+1)
        elif k==4:
            move(r,c,d);move(r,c,d+1);move(r,c,d+2)
        else:
            move(r,c,d);move(r,c,d+1);move(r,c,d+2);move(r,c,d+3)
    cnt=0
    for g in tmp_graph:
        cnt+=g.count(0)
    ans=min(cnt,ans)
print(ans)