'''def findArea(r):
    PI = 3.14
    return PI * (r*r);
print("Area of circle = %.6f" % findArea(4.5));'''
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%400==0 :
        leap = True
    elif year%4 == 0 and year%100 != 0:
        leap = True
    return leap

year = int(input())
print(is_leap(year))

