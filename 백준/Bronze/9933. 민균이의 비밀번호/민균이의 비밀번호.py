n=int(input())

dic=dict()
for i in range(n):
   tmp=input().rstrip()
   if tmp not in dic:
      dic[tmp]=1
   rtmp=tmp[::-1]
   if rtmp in dic:
      print(len(rtmp), rtmp[len(rtmp)//2])
      break