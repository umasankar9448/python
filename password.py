n=input()

#if n!=None:

    #a=n.lower()

b=""

c=""

for i in n:

    if i not in b:

        b+=i

for i in b:

    if b.index(i)%2==0:

        c+=i

    else:

        e=i

        c+=e.upper()

c=c+str(len(n))+str(len(b))

print(str(c))
