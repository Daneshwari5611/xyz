#python program to implement sequential search
x=[]
n=int(input("enter no.of elements you want to read "))
for i in range(0,n):
    item=int(input("enter the element "))
    x.append(item)
key=int(input("enter the element you want to search "))
pos=-1
for i in range(0,n):
    if(key==x[i]):
        pos=i
        break
if(pos==-1):
    print(f"{key} element is not found")
else:
    print(f"{key} element is found at {pos} position")