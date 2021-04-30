from tkinter import *


def teachers_view1(name, rno, branch, specialization, pas, update):
    root = Tk()
    root.geometry('500x600')
    root.title("UPDATE PROFILE")
    #root.iconbitmap("../dbms_project/Icons and images/3289566-assistant-educator-professor-showing-teacher-teaching_107089.ico")

    label_0 = Label(root, text="{}'s Profile".format('Loukik'), width=20, font=("bold", 20)).grid(row=0, column=3,
                                                                                                  columnspan=3)

    label_1 = Label(root, text="Name", width=20, font=("bold", 10))
    label_1.place(x=90, y=70)

    entry_1 = Entry(root)
    entry_1.insert(0, name)
    entry_1.place(x=240, y=70)

    label_2 = Label(root, text="Roll no", width=20, font=("bold", 10))
    label_2.place(x=90, y=100)

    mystr = StringVar()
    mystr.set(rno)
    entry_2 = Entry(root, textvariable=mystr, state=DISABLED)
    entry_2.place(x=240, y=100)

    #label_3 = Label(root, text="Sem", width=20, font=("bold", 10))
    #label_3.place(x=90, y=130)

    #entry_3 = Entry(root)
    #entry_3.insert(0, sem)
    #entry_3.place(x=240, y=130)

    label_4 = Label(root, text="Branch", width=20, font=("bold", 10))
    label_4.place(x=90, y=130)

    list1 = ['Computer', 'Information Technology', 'Mechanical', 'Extc', 'Electrical']
    c = StringVar()
    droplist = OptionMenu(root, c, *list1)
    droplist.config(width=15)
    c.set(branch)
    droplist.place(x=240, y=130)

    label_5 = Label(root, text="Specialization", width=20, font=("bold", 10))
    label_5.place(x=90, y=160)

    entry_5 = Entry(root)
    entry_5.insert(0, specialization)
    entry_5.place(x=240, y=160)

    Button(root, text='Change password', width=22, bg='brown', fg='white', command=pas).place(x=180, y=250)
    Button(root, text='Cancel', width=22, bg='red', fg='white', command=root.destroy).place(x=180, y=300)
    Button(root, text='Update', width=22, bg='green', fg='white', command=update).place(x=180, y=350)

    root.mainloop()


teachers_view1('loukik', '1019149', 'COMPUTERS','dbms', 1, 2)