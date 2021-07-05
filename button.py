from tkinter import *
root=Tk()
root.geometry('300x400')
#button witout any functon
myButton=Button(root,text='Click me')
myButton.pack()
myButton2=Button(root,text="Click ME",state=DISABLED)
myButton2.pack()
myButton3=Button(root,text="CLICK ME",padx=50,bg='yellow',fg='brown')
myButton3.pack()
myButton4=Button(root,text='CLICK ME',padx=50,pady=80,fg='red',bg='pink')
myButton4.pack()
root.mainloop()