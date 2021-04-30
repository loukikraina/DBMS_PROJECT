# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 19:16:55 2021

@author: LOUKIK RAINA
"""
import os
os.chdir(os.getcwd())
from student.student_class import student 
from teacher.teacher_class import teacher 
from tkinter import *
import bcrypt
import time    
import sqlite3


conn = sqlite3.connect('dbms.db')
cur = conn.cursor()


root = Tk()
root.geometry('500x500')

def login():
    root = Tk()
    root.geometry('500x500')
    root.title("Login for students")
    root.iconbitmap("Icons/studentmeets_4873.ico")

    label_0 = Label(root, text="Login form",width=20,font=("bold", 20))
    label_0.place(x=90,y=53)

    label_1 = Label(root, text="ID number:- ",width=20,font=("bold", 10))
    label_1.place(x=90,y=130)

    entry_1 = Entry(root)
    entry_1.place(x=240,y=130)

    label_2 = Label(root, text="Password",width=20,font=("bold", 10))
    label_2.place(x=90,y=180)

    entry_2 = Entry(root,show="*")
    entry_2.place(x=240,y=180)
    
    def log():
        
        
        olpass = cur.execute('''select Password,Category from Login_details where ID_no = {}'''.format(entry_1.get())).fetchone()

        salt = bcrypt.gensalt(10)
        if bcrypt.checkpw(entry_2.get().encode(),olpass[0].encode()):
            print("match")
            if olpass[1]=='S':
                print("Entering student mode")
                s = student(entry_1.get(),olpass[0])
                root.destroy()
                s.main_view()
                s.close_conn()
            else:
                print("Entering teachers mode")                
                t = teacher(entry_1.get(),olpass[0])
                root.destroy()
                t.main_view()
                t.close_conn()
            
        else:
            print("does not match")
            Label(root,text="Wrong Old password entered, try again!!!",font=("bold",12),fg= 'red').place(x=90,y=250)
            return

    Button(root, text='Login',width=20,bg='brown',fg='white',height = 1, command = log).place(x=180,y=220)
    root.mainloop()


def RegisterT():

    root = Tk()
    root.geometry('500x500')
    root.title("Registration Form")
    root.iconbitmap("Icons/check-form_116472.ico")

    label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
    label_0.place(x=90,y=53)

    label_1 = Label(root, text="Full Name: ",width=20,font=("bold", 10))
    label_1.place(x=90,y=130)

    entry_1 = Entry(root)
    entry_1.place(x=240,y=130)

    label_2 = Label(root, text="ID number: ",width=20,font=("bold", 10))
    label_2.place(x=90,y=180)

    entry_2 = Entry(root)
    entry_2.place(x=240,y=180)

    label_3 = Label(root, text="Subject ID: ",width=20,font=("bold", 10))
    label_3.place(x=90,y=210)

    entry_3 = Entry(root)
    entry_3.place(x=240,y=210)

    label_4 = Label(root, text="Department: ",width=20,font=("bold", 10))
    label_4.place(x=90,y=260)

    list1 = ['COMPUTERS','INFORMATION TECHNOLOGY','MECHANICAL','EXTC','ELECTRICAL']
    c=StringVar(root)
    droplist=OptionMenu(root,c, *list1)
    droplist.config(width=15)
    c.set('Select your branch') 
    droplist.place(x=240,y=250)

    label_5 = Label(root, text="Password",width=20,font=("bold", 10))
    label_5.place(x=90,y=300)
    entry_5 = Entry(root,show="*")
    entry_5.place(x=240,y=300)

    label_6 = Label(root, text="Confirm Password",width=20,font=("bold", 10))
    label_6.place(x=90,y=340)
    entry_6 = Entry(root,show="*")
    entry_6.place(x=240,y=340)
    
    def register_db():
        if entry_5.get()!=entry_6.get():
            print("Passwords dont match!!!!")
            Label(root,text="Passwords dont match! enter again!!!",font=("bold",12),fg= 'red').place(x=90,y=450)
            return
        salt = bcrypt.gensalt(10)
        
        hashed1 = bcrypt.hashpw(entry_5.get().encode(), salt)
                
        try:
            query  = "insert into Login_details values('{}','{}','{}')".format(entry_2.get(),hashed1.decode(),'T')
            cur.execute(query)
            query  = "insert into Teacher values('{}','{}',{},'{}','{}')".format(entry_1.get().split()[0].strip(),
                            entry_1.get().split()[1].strip(),entry_2.get(),entry_3.get().strip(),c.get())
            cur.execute(query)
        except Exception as e:
            print(e)
        
        conn.commit()
        Label(root,text="Registered!!!",font=("bold",12),fg= 'red').place(x=90,y=420)
        time.sleep(1)
        root.destroy()
            
            
    
    Button(root, text='Register',width=22,bg='brown',fg='white', command = register_db).place(x=180,y=380)
    root.mainloop()


def RegisterS():

    root = Tk()
    root.geometry('500x500')
    root.title("Registration Form")
    root.iconbitmap("Icons/check-form_116472.ico")

    label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
    label_0.place(x=90,y=53)

    label_1 = Label(root, text="Full Name",width=20,font=("bold", 10))
    label_1.place(x=90,y=130)

    entry_1 = Entry(root)
    entry_1.place(x=240,y=130)

    label_2 = Label(root, text="Roll no",width=20,font=("bold", 10))
    label_2.place(x=90,y=180)

    entry_2 = Entry(root)
    entry_2.place(x=240,y=180)

    label_3 = Label(root, text="Semester",width=20,font=("bold", 10))
    label_3.place(x=90,y=210)

    entry_3 = Entry(root)
    entry_3.place(x=240,y=210)

    label_4 = Label(root, text="Branch",width=20,font=("bold", 10))
    label_4.place(x=90,y=260)

    list1 = ['COMPUTERS','INFORMATION TECHNOLOGY','MECHANICAL','EXTC','ELECTRICAL']
    c=StringVar(root)
    droplist=OptionMenu(root,c, *list1)
    droplist.config(width=15)
    c.set('Select your branch') 
    droplist.place(x=240,y=250)

    label_5 = Label(root, text="Password",width=20,font=("bold", 10))
    label_5.place(x=90,y=300)
    entry_5 = Entry(root,show="*")
    entry_5.place(x=240,y=300)

    label_6 = Label(root, text="Confirm Password",width=20,font=("bold", 10))
    label_6.place(x=90,y=340)
    entry_6 = Entry(root,show="*")
    entry_6.place(x=240,y=340)
    
    label_7 = Label(root, text="Elective Id:- ",width=20,font=("bold", 10))
    label_7.place(x=90,y=380)

    entry_7 = Entry(root)
    entry_7.place(x=240,y=380)
    
    label_9 = Label(root, text="Seat No.:- ",width=20,font=("bold", 10))
    label_9.place(x=90,y=420)

    entry_9 = Entry(root)
    entry_9.place(x=240,y=420)
    
    def register_db():
        if entry_5.get()!=entry_6.get():
            print("Passwords dont match!!!!")
            Label(root,text="Passwords dont match! enter again!!!",font=("bold",12),fg= 'red').place(x=90,y=450)
            return
        salt = bcrypt.gensalt(10)
        hashed1 = bcrypt.hashpw(entry_5.get().encode(), salt)
                
        try:
            query  = "insert into Login_details values('{}','{}','{}')".format(entry_2.get(),hashed1.decode(),'S')
            cur.execute(query)
            query  = "insert into Student values('{}','{}',{},'{}',{},{},{},'{}')".format(entry_1.get().split()[0].strip(),
                            entry_1.get().split()[1].strip(),entry_3.get().strip(),c.get(),entry_2.get(),1,entry_9.get().strip(),entry_7.get().strip())
            cur.execute(query)
        except Exception as e:
            print(e)
        
        conn.commit()
        Label(root,text="Registered!!!",font=("bold",12),fg= 'red').place(x=90,y=420)
        time.sleep(1)
        root.destroy()
    
    
    
    Button(root, text='Register',width=22,bg='brown',fg='white', command = register_db).place(x=180,y=450)
    root.mainloop()



root.title("Academics Tracker")
##please include your file path for the icon here
root.iconbitmap("Icons/4023873-brain-learning-machine-machine-learning-ml_112855.ico")

##please include your file path for the background here
##bg
bg = PhotoImage(file = "Icons/bg.png")
my_label = Label(root, image = bg)
my_label.place(x = 0, y= 0, relwidth = 1, relheight = 1)

##buttons
Button(root, text='Exit',width=20,height = 3,bg='brown',fg='white',activebackground = 'blue',command=root.destroy).place(x=154,y=375)
Button(root, text='Login',width=20,height = 3,bg='brown',fg='white',activebackground = 'blue',command = login).place(x=154,y=150)
Button(root, text='Register(Student)',width=20,height = 3,bg='brown',fg='white',activebackground = 'blue',command =RegisterS ).place(x=154,y=225)
Button(root, text='Register(Teacher)',width=20,height = 3,bg='brown',fg='white',activebackground = 'blue',command =RegisterT ).place(x=154,y=300)

root.mainloop()
