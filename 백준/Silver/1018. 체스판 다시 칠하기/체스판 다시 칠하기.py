n,m=map(int,input().split())
arr=list( list(x) for _ in range(n) for x in input().split() ) 
#print(arr)

w_cnt,b_cnt=0,0
cnt=list()
def check(a,b,w_cnt,b_cnt):
    for i in range(a,a+8):
        for j in range(b,b+8):
            if (i+j)%2==0:
                if arr[i][j]!='W':
                    w_cnt+=1
                else:
                    b_cnt+=1
            else:
                if arr[i][j]!='W':
                    b_cnt+=1
                else:
                    w_cnt+=1
    return w_cnt,b_cnt
for a in range(n-7):
    for b in range(m-7):
        w_cnt,b_cnt=check(a,b,0,0)
        cnt.append(w_cnt)
        cnt.append(b_cnt)
        
print(min(cnt))