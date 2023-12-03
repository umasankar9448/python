n=input()
v="aeiou"
l=[]
for i in n:
   if i not in v:
       l.append(i)
b=l[::-1]
for j in b:
    print(j,end="")
        
