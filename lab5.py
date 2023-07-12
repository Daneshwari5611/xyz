#python program to check a numberis prime or not
n=int(input('enter the number '))
flag=False
for i in range(2,n//2+1):
    if(n%i==0):
        flag=True
        break
if(flag==True):
    print(f'{n} is not a prime number')
else:
    print(f'{n} is pime number')