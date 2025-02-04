import sys
input=sys.stdin.readline

arr=input().rstrip()
dic1=dict()
dic2=dict()
dic2['P']=13
dic2['K']=13
dic2['H']=13
dic2['T']=13
for i in range(0,len(arr)-2,3):
    res=arr[i:i+3]
    if res in dic1:
        print('GRESKA')
        exit(0)
    else:
        dic1[res]=1
    k=res[0]
    dic2[k]-=1

print(*dic2.values())