from collections import deque

def solution(n, wires):
    answer = -1
    tree=list([0]*(n+1) for _ in range(n+1))
    for x,y in wires:
        print(x,y)
        tree[x][y]=1
        tree[y][x]=1
    
    print(tree)
    
    def count(a,b):
        visited=[0]*(n+1)
        q=deque()
        q.append(a)
        visited[a]=1
        visited[b]=1
        cnt=1
        while q:
            p=q.popleft()
            for idx,np in enumerate(tree[p]):
                if np==1:
                    if not visited[idx]:
                        # print(idx)
                        q.append(idx)
                        visited[idx]=1
                        cnt+=1
        return cnt
          
    # c=count(1,3)
    # c1=count(3,1)
    # print(c,c1)
    # return

    l=list()
    for i in range(1,n+1):
        for j in range(1,n+1):
            if tree[i][j]==1:
                print(i,j)
                i_count=count(i,j)
                j_count=count(j,i)
                print(i_count,j_count)
                # return
                l.append(abs(i_count-j_count))
    # print(l)
    answer=min(l)
    return answer