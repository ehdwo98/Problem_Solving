import sys

while True:
   try:
      tmp=input().rstrip()
      if not tmp:
         break
      print(tmp)
   except EOFError:
      break