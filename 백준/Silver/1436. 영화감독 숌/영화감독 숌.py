n=int(input())

cnt,res=0,666

while 1:
    if '666' in str(res):
        cnt+=1
    if cnt==n:
        print(res)
        break
    res+=1