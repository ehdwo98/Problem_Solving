def check(level):
   if level=="A+":
      l=4.5
   elif level=="A0":
      l=4.0
   elif level=="B+":
      l=3.5
   elif level=="B0":
      l=3.0
   elif level=="C+":
      l=2.5
   elif level=="C0":
      l=2.0
   elif level=="D+":
      l=1.5
   elif level=="D0":
      l=1.0
   elif level=="F":
      l=0.0
   return l

ans=0
score_sum=0
for _ in range(20):
   name,score,level=input().split()
   if level=="P":
      continue
   score=float(score)
   l=check(level)
   ans+=float(score*l)
   score_sum+=score

print(float(ans/score_sum))