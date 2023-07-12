import cmath
a=int(input("enter the value for a"))
b=int(input("enter the value for b"))
c=int(input("enter the value for c"))
d=b*b-4*a*c
root1=(-b+cmath.sqrt(d))/2*a
root2=(-b-cmath.sqrt(d))/2*a
if(d>0):
    print(f"roots are real root1={root1} root2={root2}")
elif(d<0):
    print(f"roots are imaginary root1={root1} root2={root2}")
else:
    print(f"roots are equal root1=root2={root1}")