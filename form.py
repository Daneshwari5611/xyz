#step 1 import tkinter module
from tkinter import *
import tkinter.messagebox as msgbox
form=Tk()
form.geometry("800x800")
lblftext=Label(form,text="username",font=("Arial",14,"bold"))
lblftext.grid(row=1,column=1)
etftext=Entry(form,width=50)
etftext.grid(row=1,column=2)
lblstext=Label(form,text="password",font=("Arial",14,"bold"))
lblstext.grid(row=2,column=1)
etstext=Entry(form,width=50,show="*")
etstext.grid(row=2,column=2)
btnsubmit=Button(form,text="submit",font=("Arial",14,"bold"))
btnsubmit.grid(row=4,column=2)
def reset():
    etftext.delete(0,END)
    etstext.delete(0,END)
btnreset=Button(form,text="Reset",command=reset,font=("Arial",14,"bold"))
btnreset.grid(row=4,column=3)
form.mainloop()