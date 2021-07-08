from tkinter import *
root=Tk()
root.title('using grid')
#creating a lable widget
my_lable=Label(root,text="Tkinter programming beginner")
my_lable2=Label(root,text="my name is manjesh silwal")
my_lable3=Label(root,text="softwrica")
#sahoing it in the screen in the basis of row and column
#that do not move having constant position
my_lable.grid(row=2,column=3)
my_lable2.grid(row=1,column=1)
my_lable3.grid(row=0,column=0)
root.mainloop()