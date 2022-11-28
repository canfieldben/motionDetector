from tkinter import *
import winsound

top = Tk()
top.title('Salty Inc. Security')
top.geometry("270x30")
L1 = Label(top, text="Activation Code")
L1.pack(side=LEFT)
E1 = Entry(top, show="$", bd=5)
E1.pack(side=RIGHT)


def motion_run():
    return


def check_val():
    if E1.get() == 'cabinVT!1':
        print('test')
        motion_run()
    else:
        print('playing sound')
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)


submit_btn = Button(top, text="Submit", width=10, command=check_val)
submit_btn.pack(side=RIGHT)

top.mainloop()
