#python progam to implement selection sort
x=[]
n=int(input("enter no.of elements you want to read "))
for i in range(0,n):
    item=int(input("enter the element "))
    x.append(item)
print('list of elements')
print(x)
for i in range(0,n):
    pos=i
    for j in range(i+1,n):
        if(x[j]<x[pos]):
            pos=j
    temp=x[i]
    x[i]=x[pos]
    x[pos]=temp
print('soted elements are')
print(x)