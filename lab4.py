n=int(input("enter the iimit"))
for i in range(1,11,1):
    for j in range(2,n+1,1):
        print(f"{i*j}",end="\t")
    print("\n")
    