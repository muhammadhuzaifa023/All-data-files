import tkinter
window=tkinter.Tk()
def greeting():
    tkinter.Label(window,text='Hello Hw are you all???').pack()
    no=5
    print(no)
    return no

tkinter.Button(window,command=greeting,text='Click it!',bg='grey',fg='black').pack()

window.mainloop()
