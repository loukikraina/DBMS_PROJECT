from tkinter import *


def student_view1(mi, pre, upd):
    root = Tk()
    # root.geometry('600x700')
    root.title("STUDENT PROFILE")
    #root.iconbitmap("./3289566-assistant-educator-professor-showing-teacher-teaching_107089.ico")

    label_0 = Label(root, text="{}'s Profile".format('Loukik'), width=20, font=("bold", 20)).grid(row=0, column=0,
                                                                                                  columnspan=3)

    label_1 = Label(root, text="Name:- ", font=("bold", 10), fg='red')
    label_1_a = Label(root, text="Loukik Raina", font=("bold", 10))

    label_2 = Label(root, text="Roll no:- ", font=("bold", 10), fg='red')
    label_2_a = Label(root, text="1019149", font=("bold", 10))

    label_3 = Label(root, text="Specialization:- ", font=("bold", 10), fg='red')
    label_3_a = Label(root, text="Database Management", font=("bold", 10))

    label_4 = Label(root, text="Branch:- ", font=("bold", 10), fg='red')
    label_4_a = Label(root, text="Computer", font=("bold", 10))

    label_7 = Label(root, text='Gender', font=("bold", 10), fg='red')
    label_7_a = Label(root, text='Gender', font=("bold", 10))

    label_1.grid(row=1, column=0, sticky=W, pady=2)
    label_1_a.grid(row=1, column=1, sticky=W, pady=2)

    label_2.grid(row=2, column=0, sticky=W, pady=2)
    label_2_a.grid(row=2, column=1, sticky=W, pady=2)

    label_3.grid(row=3, column=0, sticky=W, pady=2)
    label_3_a.grid(row=3, column=1, sticky=W, pady=2)

    label_4.grid(row=4, column=0, sticky=W, pady=2)
    label_4_a.grid(row=4, column=1, sticky=W, pady=2)

    label_7.grid(row=5, column=0, sticky=W, pady=2)
    label_7_a.grid(row=5, column=1, sticky=W, pady=2)

    #Button(root, text='Marks info', width=22, bg='brown', fg='white', command=mi).grid(row=6, column=0, rowspan=2,
                                                                                       #stick=S, padx=5, pady=5)
    #Button(root, text='Predict', width=22, bg='brown', fg='white', command=pre).grid(row=6, column=2, rowspan=2,
                                                                                     #stick=S, padx=5, pady=5)
    Button(root, text='Update Profile', width=22, bg='brown', fg='white', command=upd).grid(row=7, column=1, rowspan=2,
                                                                                            padx=5, pady=5)
    root.mainloop()

student_view1(120, 110, "blue")