import sys
input=sys.stdin.readline

dic = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', 
     '6':'six', '7':'seven', '8':'eight', '9':'nine', '0':'zero'}

m,n=map(int,input().split())

arr=list()
for i in range(m,n+1):
    eng=' '.join(list(dic[j] for j in str(i)))
    arr.append([eng,i])

arr.sort()
for i in range(len(arr)):
    if i%10==0 and i!=0:
        print()
    print(arr[i][1],end=' ')