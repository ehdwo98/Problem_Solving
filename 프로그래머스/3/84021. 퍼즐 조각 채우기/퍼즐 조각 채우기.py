from collections import deque

def solution(game_board, table):
    n=len(game_board)
    D=[(1,0),(-1,0),(0,1),(0,-1)]
    
    #좌표들을 (0,0)기준으로 정규화
    def norm(array):
        mr=min(r for r,c in array)
        mc=min(c for r,c in array)
        norm_array=list()
        for r,c in array:
            norm_array.append([r-mr,c-mc])
        return sorted(norm_array)
    
    #board에서 target값으로 연결된 덩어리들 찾기
    def find_shapes(board, target):
        visited=list([0]*n for _ in range(n))
        shapes=list()
        for i in range(n):
            for j in range(n):
                if board[i][j]==target and not visited[i][j]:
                    q=deque()
                    visited[i][j]=1
                    q.append([i,j])
                    tmp=list()
                    while q:
                        x,y=q.popleft()
                        tmp.append([x,y])
                        for dx,dy in D:
                            nx,ny=x+dx,y+dy
                            if 0<=nx<n and 0<=ny<n:
                                if board[nx][ny]==target and not visited[nx][ny]:
                                    visited[nx][ny]=1
                                    q.append([nx,ny])
                    shapes.append(norm(tmp))
        return shapes
    
    #모양을 90도 회전
    def rotate(shape):
        rotated=list()
        for r,c in shape:
            rotated.append([c,-r])
        return norm(rotated)
    
    empties=find_shapes(game_board,0)
    # print(empties)
    blocks=find_shapes(table,1)
    # print(blocks)
    used=[0]*len(blocks)
    answer=0
    
    for empty in empties:
        for i in range(len(blocks)):
            if used[i]:
                continue
            block=blocks[i]
            if len(empty)!=len(block):
                continue
            current=block
            for _ in range(4):
                if empty==current:
                    answer+=len(empty)
                    used[i]=1
                    break
                current=rotate(current)
            if used[i]:
                break
    
    return answer