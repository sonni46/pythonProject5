import sys
from tkinter import *

def TimeTable():
    print('\n')
    for x in range(1,11):
        m = int(EnterTable.get())
        print(f"\t\t, {x} x {m} = {x * m}")

root = Tk()
root.geometry('250x250')
root.title('Multiplication Table')


EnterTable = StringVar()

lab = Label(root,text='       Multiplication TimeTable',fg='Black',font=30,).grid(row=1,column=6)
lab = Label(root,text='                                     ').grid(row=2,column=6)
ent = Entry(root,textvariable=EnterTable,justify='center').grid(row=3,column=6)
lab = Label(root,text='                                            ').grid(row=4,column=6)

button = Button(root,text='Time Table',command=TimeTable,).grid(row=5,column=6)
lab = Label(root,text='                                   ').grid(row=6,column=6)
quit = Button(root,text='Quit',bg='red',fg='black',command=root.destroy).grid(row=7,column=6)

root.mainloop()
