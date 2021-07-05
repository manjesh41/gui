from tkinter import*
root=Tk()
root.geometry('300x300')
c=Canvas(root,height='250',width='300',bg='red')
l=c.create_arc(10,50,240,250,extent=280,fill='blue')
c.pack()

root.mainloop()
