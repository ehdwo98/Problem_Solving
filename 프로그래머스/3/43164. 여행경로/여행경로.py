#백트래킹 DFS

def dfs(path,tickets,used,n):
    if len(path)==n+1:
        return 1
    for i,values in enumerate(tickets):
        s,e=values
        if not used[i] and path[-1]==s:
            used[i]=1
            path.append(e)
            if dfs(path,tickets,used,n):
                return 1
            used[i]=0
            path.pop()
    return 0

def solution(tickets):
    tickets.sort()
    n=len(tickets)
    used=[0]*n
    path=["ICN"]
    dfs(path,tickets,used,n)
    return path