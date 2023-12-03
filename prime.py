"""for num in range (1,200):
    if all(num%i!=0 for i in range(2,num)):
        print(num)"""
l=[12,3,48,89,23,8,78,554,12,12,33,3,8]
"""l.sort(reverse=True)
print(l)"""
"""print(l[::-1])
x=[]
for i in l:
    if i not in x:
        x.append(i)
print(x)
"""
for row in range(6):
    for col in range(7):
        if(((row==0) and (col%3!=0)) or ((row==1) and (col%3==0)) or (row-col==2) or (row+col==8)):
            print("*",end="")
        else:
            print("",end="")
    print()
