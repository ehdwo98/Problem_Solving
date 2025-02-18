import sys
input=sys.stdin.readline

a,b=input().split()
ans1=0
ans2=0
for x in [a,b]:
    res1=''
    res2=''
    for i in range(len(x)):
        if x[i]=='5':
            res1+='5'
            res2+='6'
        elif x[i]=='6':
            res1+='5'
            res2+='6'
        else:
            res1+=x[i]
            res2+=x[i]
    # print(res)
    ans1+=int(res1)
    ans2+=int(res2)
print(ans1,ans2)