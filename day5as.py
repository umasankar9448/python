n=int(input())
l=[]
a,b,c=input().split()
l.append(a)
l.append(b)
l.append(c)
d=sorted(l)
for i in d:
    print(i,end=" ")

