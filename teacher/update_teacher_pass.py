from tkinter import *
import bcrypt
import time


def teachers_view(name, rno, sem, branch, pas, update, hashed):##change the attributes here
    root = Tk()
    root.geometry('500x600')
    root.title("UPDATE PROFILE PASSWORD")
    root.iconbitmap("../Icon/3289566-assistant-educator-professor-showing-teacher-teaching_107089.ico")

    def pass_check():
        if entry_2.get() != entry_3.get():
            print("Passwords don't match!")
            Label(root, text="Passwords don't match! Enter again", font=("bold", 12), fg='red').place(x=90, y=170)
        else:
            '''old_pass = entry_1.get()
            if bcrypt.checkpw(old_pass.encode(), hashed.encode()):
                print("match")
            else:
                print("does not match")'''

            salt = bcrypt.gensalt()
            hashed1 = bcrypt.hashpw(entry_2.get().encode(), salt)
            Label(root, text="Passwords successfully changed!", font=("bold", 12), fg='red').place(x=90, y=170)
            time.sleep(1)
            root.destroy()
            print(hashed1)

    label_0 = Label(root, text="{}'s Profile".format("Dakshyani Ma'am"), width=20, font=("bold", 20)).grid(row=0, column=3,
                                                                                                  columnspan=3)

    label_1 = Label(root, text="Old Password", width=20, font=("bold", 10))
    label_1.place(x=90, y=70)

    entry_1 = Entry(root, show="*")
    entry_1.place(x=240, y=70)

    label_2 = Label(root, text="New Password", width=20, font=("bold", 10))
    label_2.place(x=90, y=100)

    entry_2 = Entry(root, show="*")

    entry_2.place(x=240, y=100)

    label_3 = Label(root, text="Confirm new password", width=20, font=("bold", 10))
    label_3.place(x=90, y=130)

    entry_3 = Entry(root, show="*")

    entry_3.place(x=240, y=130)

    Button(root, text='Change password', width=22, bg='green', fg='white', command=pass_check).place(x=180, y=250)
    Button(root, text='Cancel', width=22, bg='red', fg='white', command=root.destroy).place(x=180, y=300)

    root.mainloop()

teachers_view('Aaditee',46, 4, 'computer', '1234', '12345678','********')