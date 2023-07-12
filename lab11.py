#python pogram to read and write files
file=None
def showMenu():
    print("student admission system")
    print("1-->new admission")
    print("2-->display all")
    print("3-->exit")
def newAdmission():
    global file
    uucmsno=input("enter uucms number:")
    name=input("enter name of the student:")
    file=open("student.csv","a")
    s=f"{uucmsno},{name}\n"
    file.write(s)
    file.close()
    print("student admission done successfully")
def displayAll():
    global file
    file=open("student.csv","r")
    data=file.read()
    lines=data.split("\n")
    print(lines)
    lines=lines[0:len(lines)-1]
    for l in lines:
        s=l.split(",")
        print(f"{s[0]}\t{s[1]}")
    file.close()
    print(lines)
#begin of main program calculations above
while True:
    showMenu()
    choice=int(input("enter your choice"))
    if(choice==1):
        newAdmission()
    elif(choice==2):
        displayAll()
    elif(choice==3):
        break
    else:
        print("invalid choice")
