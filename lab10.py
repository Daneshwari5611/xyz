stack=[]
size=5
top=-1
while True:
    print("stack operation")
    print("1-->push")
    print("2-->pop")
    print("3-->display") 
    print("4-->exit")
    choice=int(input("enter your choice"))
    if(choice==1):
        if(top==size-1):
            print("stack is full")
        else:
            top=top+1
            item=int(input("enter your element"))
            stack.append(item)
            print(f"{item} is pushed onto stack")
    elif(choice==2):
        if(top==-1):
            print("stack is empty")
        else:
            item=stack[top]
            top=top-1
            stack.pop()
            print(f"{item} is deleted from the stack")
    elif(choice==3):
        if(top==-1):
            print("stack is empty")
        else:
            print("stack elements as folllows")
            for i in range(0,top+1):
                print(stack[i])
    else:
        break
        
        
        