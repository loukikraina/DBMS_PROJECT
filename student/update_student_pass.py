# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 14:39:48 2021

@author: LOUKIK RAINA
"""

from tkinter import *
import bcrypt
import time     
    
        
    

def student_view3(name,rno,sem,branch,pas,update,hashed):

    root = Tk()
    root.geometry('500x600')
    root.title("UPDATE PROFILE PASSWORD")
    root.iconbitmap("./4023873-brain-learning-machine-machine-learning-ml_112855.ico")

    
    def pass_check():
        if entry_2.get()!=entry_3.get():
            print("Passwords dont match!!!!")
            Label(root,text="Passwords dont match! enter again!!!",font=("bold",12),fg= 'red').place(x=90,y=170)
        else: 
            '''old_pass = entry_1.get()
            if bcrypt.checkpw(old_pass.encode(), hashed.encode()):
                print("match")
            else:
                print("does not match")'''
            
            salt = bcrypt.gensalt()
            hashed1 = bcrypt.hashpw(entry_2.get().encode(), salt)
            Label(root,text="Passwords successfully changed!!!",font=("bold",12),fg= 'red').place(x=90,y=170)
            time.sleep(1)
            root.destroy()
            print(hashed1)
    
    label_0 = Label(root, text="{}'s Profile".format('Loukik'),width=20,font=("bold", 20)).grid(row = 0,column = 3,columnspan = 3)
    
    
    
    label_1 = Label(root, text="Old Password",width=20,font=("bold", 10))
    label_1.place(x=90,y=70)
    
    entry_1 = Entry(root,show="*")
    entry_1.place(x=240,y=70)
    
    label_2 = Label(root, text="New Password",width=20,font=("bold", 10))
    label_2.place(x=90,y=100)
    
    
    entry_2 = Entry(root,show="*")
 
    entry_2.place(x=240,y=100)
    
    label_3 = Label(root, text="Confirm new password",width=20,font=("bold", 10))
    label_3.place(x=90,y=130)
    
    entry_3 = Entry(root,show="*")
   
    entry_3.place(x=240,y=130)

    
    Button(root, text='Change password',width=22,bg='green',fg='white',command = pass_check).place(x=180,y=250)
    Button(root, text='Cancel',width=22,bg='red',fg='white',command = root.destroy).place(x=180,y=300)

    root.mainloop()

#student_view1('loukik','1019149','4','COMPUTERS',1,2,'hello')



