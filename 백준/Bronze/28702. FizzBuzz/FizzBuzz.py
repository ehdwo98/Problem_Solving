for i in range(3):
   tmp=input().rstrip()
   if tmp.isdigit():
      tmp=int(tmp)
      res_i=tmp+(3-i)
# print(res_i)
res=str(res_i)
res=list(map(int,res))
# print(res)
if (res[-1]==0 or res[-1]==5) and sum(res)%3==0:
   print('FizzBuzz')
elif  (res[-1]==0 or res[-1]==5) and sum(res)%3!=0:
   print('Buzz')
elif res[-1]!=0 and res[-1]!=5 and sum(res)%3==0:
   print('Fizz')
else:
   print(res_i)