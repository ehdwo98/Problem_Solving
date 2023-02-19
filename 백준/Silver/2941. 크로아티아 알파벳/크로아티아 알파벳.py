croAlpa=['c=','c-','dz=','d-','lj','nj','s=','z=']
    
word=input()

for i in croAlpa:
    word=word.replace(i,'@')

print(len(word))