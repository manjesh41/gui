from tkinter import *
root=Tk()
e1=Entry(root,width=50,fg='red',bg='yellow',borderwidth=5)
e1.pack()
def my_click():
    textoutput='hello'+ e1.get()

    mylable =Label(root, text=textoutput)
    mylable.pack()

    mybutton=Button(root,text=textoutput)
    mybutton.pack()

mybutton=Button(root,text='Click Me',command=my_click)
mybutton.pack()
root.mainloop()
