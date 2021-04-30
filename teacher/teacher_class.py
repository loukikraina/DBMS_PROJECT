# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 14:39:48 2021

@author: LOUKIK RAINA
"""

from tkinter import *
import bcrypt
import time    
import sqlite3 
import os
        

class teacher:
    
    teacher_id = None
    conn = None
    cur = None
    teacher = None
    sub = None
    query1 = None
    query2 = None
    query3 = None
    query4 = None
    opass = None

    
    def __init__(self,tid,oldpass):
        print(os.getcwd())
        self.teacher_id = tid
        self.opass = oldpass
        self.conn = sqlite3.connect('dbms.db')
        self.cur = self.conn.cursor()
        self.query1 = "SELECT * FROM teacher where t_id = '{}'".format(self.teacher_id)
        self.query2 = '''select ia_1,ia_2,end_sem from Student,Marks WHERE
                marks.seat_no = Student.seat_no
                and (student.semester,student.branch,marks.sub_id) in 
                ( select sem,branch,Subjects.sub_id from Courses,Subjects 
                where courses.course_id = Subjects.course_id
                and Subjects.sub_id = '{}'); '''
        '''self.query3 = 'SELECT ia_1,ia_2,end_sem from Marks
                    where sub_id = '%s' 
                    and seat_no in(select seat_no from teacher
                    where roll_no = '{}' )'.format(self.teacher_id)'''
                    
        self.query4 = '''UPDATE teacher set fname = '%s',dname = '%s',sub_id = '%s',department = '%s' 
            where t_id = '{}' '''.format(self.teacher_id)
        self.teacher = self.cur.execute(self.query1).fetchone()
        #self.stu = self.cur.execute(self.query2).fetchall()
    
    def refresh(self):
        
        self.teacher = self.cur.execute(self.query1).fetchone()
        #self.sub = self.cur.execute(self.query2).fetchall()
        
    def main_view(self):

        root = Tk()
        #root.geometry('600x700')
        root.title("teacher PROFILE")
        root.iconbitmap("Icons/4023873-brain-learning-machine-machine-learning-ml_112855.ico")
    
        
        
        label_0 = Label(root, text="{}'s Profile".format(self.teacher[0]),width=20,font=("bold", 20)).grid(row = 0,column = 0,columnspan = 3)
        
        
        label_1 = Label(root, text="Name:- ",font=("bold", 12),fg = 'red')
        label_1_a = Label(root, text="{} {}".format(self.teacher[0],self.teacher[1]),font=("bold", 10))
        
        
        label_2 = Label(root, text="Teacher Id:- ",font=("bold", 12),fg = 'red')
        label_2_a = Label(root, text="{}".format(self.teacher[2]),font=("bold", 10))
        
        
        label_3 = Label(root, text="Subject Id:- ",font=("bold", 12),fg = 'red')
        label_3_a = Label(root, text="{}".format(self.teacher[3]),font=("bold", 10))
        
        
        label_4 = Label(root, text="Department:- ",font=("bold", 12),fg = 'red')
        label_4_a = Label(root, text="{}".format(self.teacher[4]),font=("bold", 10))
        
        
        '''label_7 = Label(root,text = 'Seat no:- ', font = ("bold",12),fg = 'red')
        label_7_a = Label(root,text="{}".format(self.teacher[5]), font = ("bold",10))'''
        
        label_1.grid(row = 1, column = 0, sticky = W, pady = 2)
        label_1_a.grid(row = 1, column = 1, sticky = W, pady = 2)
        
        label_2.grid(row = 2, column = 0, sticky = W, pady = 2)
        label_2_a.grid(row = 2, column = 1, sticky = W, pady = 2)
        
        label_3.grid(row = 3, column = 0, sticky = W, pady = 2)
        label_3_a.grid(row = 3, column = 1, sticky = W, pady = 2)
        
        label_4.grid(row = 4, column = 0, sticky = W, pady = 2)
        label_4_a.grid(row = 4, column = 1, sticky = W, pady = 2)
        
        '''label_7.grid(row = 5, column = 0, sticky = W, pady = 2)
        label_7_a.grid(row = 5, column = 1, sticky = W, pady = 2)'''
        
        
        
        
        Button(root, text='Enter Marks',width=22,bg='brown',fg='white',command = self.marksheet).grid(row = 6, column = 0, rowspan = 2, stick = S, padx = 5, pady = 5)
        #Button(root, text='Predict',width=22,bg='brown',fg='white',command = self.cgpa_predict).grid(row = 6, column = 2, rowspan = 2, stick = S, padx = 5, pady = 5)
        Button(root, text='Update Profile',width=22,bg='brown',fg='white',command = self.update).grid(row = 6, column = 2, rowspan = 2, padx = 5, pady = 5)
        Button(root, text='Exit',width=22,bg='IndianRed4',fg='yellow',command = root.destroy).grid(row = 6, column = 1, rowspan = 2, padx = 5, pady = 5)

        root.mainloop()    
    
    



    def update(self):
    
        root = Tk()
        root.geometry('500x600')
        root.title("UPDATE PROFILE")
        root.iconbitmap("Icons/4023873-brain-learning-machine-machine-learning-ml_112855.ico")
    
        
        def up():
            try:
                self.query4 = '''UPDATE teacher set fname = '{}',dname = '{}',sub_id = '{}',department = '{}' 
                where t_id = '{}' '''.format(entry_1.get().split()[0].strip(),entry_1.get().split()[1].strip(),entry_3.get().strip(),c.get().strip(),entry_2.get().strip())
                self.cur.execute(self.query4)
                print(self.query4)
            except Exception as e:
                print(e)
                Label(root,text="Profile didnt updated, error occured!!",font=("bold",12),fg= 'red').place(x=90,y=200)
               
            try:
                self.conn.commit()
                Label(root,text="Profile Updated!!",font=("bold",12),fg= 'red').place(x=50,y=210)
                print('done update')
            except:
                self.conn.rollback()
                Label(root,text="Profile didnt updated, error occured!!",font=("bold",12),fg= 'red').place(x=90,y=200)
                print("not update")
            self.refresh()
            time.sleep(1)
            root.destroy()

            
            
            
            
            
            
        label_0 = Label(root, text="{}'s Profile".format(self.teacher[0]),width=20,font=("bold", 20)).grid(row = 0,column = 3,columnspan = 3)
        
        
        
        label_1 = Label(root, text="Name",width=20,font=("bold", 10))
        label_1.place(x=90,y=70)
        
        entry_1 = Entry(root)
        entry_1.insert(0,self.teacher[0]+" "+self.teacher[1])
        entry_1.place(x=240,y=70)
        
        label_2 = Label(root, text="Teacher Id: ",width=20,font=("bold", 10))
        label_2.place(x=90,y=100)
        
        mystr = StringVar(root,value = self.teacher[2])
        #mystr.set(value = '1019149')
        #mystr.set('{}'.format(self.teacher[2]))
        entry_2 = Entry(root, textvariable=mystr, state=DISABLED)
        entry_2.place(x=240,y=100)
        
        label_3 = Label(root, text="Subject_id",width=20,font=("bold", 10))
        label_3.place(x=90,y=130)
        
        entry_3 = Entry(root)
        entry_3.insert(END,self.teacher[3])
        entry_3.place(x=240,y=130)
        
        label_4 = Label(root, text="Department",width=20,font=("bold", 10))
        label_4.place(x=90,y=160)
        
        list1 = ['COMPUTERS','INFORMATION TECHNOLOGY','MECHANICAL','EXTC','ELECTRICAL']
        c=StringVar(root, value = self.teacher[4])
        droplist=OptionMenu(root,c, *list1)
        droplist.config(width=15)
        #c.set(str(self.teacher[4])) 
        droplist.place(x=240,y=160)
    
        
        Button(root, text='Change password',width=22,bg='brown',fg='white',command = self.pass_change).place(x=180,y=250)
        Button(root, text='Cancel',width=22,bg='red',fg='white',command = root.destroy).place(x=180,y=300)
        Button(root, text='Update',width=22,bg='green',fg='white',command=up).place(x=180,y=350)
    
        root.mainloop()
    

    def marksheet(self,state_v = True ):
    
        root = Tk()
        #root.geometry('600x700')
        root.title("teacher PROFILE")
        root.iconbitmap("Icons/4023873-brain-learning-machine-machine-learning-ml_112855.ico")
    
        
        
        label_0 = Label(root, text="{}'s Marks Portal".format(self.teacher[0]),width=20,font=("bold", 20)).grid(row = 0,column = 1,columnspan = 3,rowspan = 2)
           
        Label(root, text = 'Student Name', borderwidth=3, font=("bold", 14), fg = 'green',bg = 'yellow').grid(row = 2, column = 0, columnspan = 2)
        Label(root, text = 'Roll NO', borderwidth=3, font=("bold", 14), fg = 'green',bg = 'yellow').grid(row = 2, column = 2, columnspan = 2)
        Label(root, text = 'IA 1', borderwidth=3, font=("bold", 14), fg = 'green',bg = 'yellow').grid(row = 2, column = 4, columnspan = 2)
        Label(root, text = 'IA 2', borderwidth=3, font=("bold", 14), fg = 'green',bg = 'yellow').grid(row = 2, column = 6, columnspan = 2)
        Label(root, text = 'ENDSEM', borderwidth=3, font=("bold", 14), fg = 'green',bg = 'yellow').grid(row = 2, column = 8, columnspan = 2)
        query = '''select fname,roll_no from student
                where (student.semester,student.branch) 
                in ( select sem,branch from Courses,Subjects 
                    where courses.course_id = Subjects.course_id
                    and Subjects.sub_id = '{}');'''.format(self.teacher[3])
        print(query)
        names = self.cur.execute(query).fetchall()
        print(names)
        
        def up():
            root = Tk()
        #root.geometry('600x700')
            root.title("Update marks")
            root.iconbitmap("Icons/4023873-brain-learning-machine-machine-learning-ml_112855.ico")
            label_0 = Label(root, text="{}'s Marks Portal".format(self.teacher[0]),width=20,font=("bold", 20)).grid(row = 0,column = 1,columnspan = 3,rowspan = 2)
            Label(root, text = 'Roll no', borderwidth=3, font=("bold", 14), fg = 'green',bg = 'yellow').grid(row = 2, column = 1, columnspan = 2)
            entry_1 = Entry(root)
            entry_1.grid(row = 2, column = 4, columnspan = 2)
            
            def query1(e1g):
                marks1 = self.cur.execute('''select DISTINCT(marks.seat_no),ia_1,ia_2,end_sem from Student,Marks WHERE marks.seat_no = Student.seat_no
                    and roll_no = '{}' and marks.sub_id = '{}' ; '''.format(e1g,self.teacher[3])).fetchone()
                print(marks1)
                marks2 = marks1
                if not marks1:
                    marks1 = ['nil','nil','nil','nil']
                    
                Label(root, text = 'IA 1', borderwidth=3, font=("bold", 14), fg = 'green',bg = 'yellow').grid(row = 6, column = 1, columnspan = 2)
                Label(root, text = 'IA 2', borderwidth=3, font=("bold", 14), fg = 'green',bg = 'yellow').grid(row = 8, column = 1, columnspan = 2)
                Label(root, text = 'ENDSEM', borderwidth=3, font=("bold", 14), fg = 'green',bg = 'yellow').grid(row = 10, column = 1, columnspan = 2)
                entry_2 = Entry(root)
                entry_2.insert(END,marks1[1])
                entry_2.grid(row = 6, column = 4, columnspan = 2)
                entry_3 = Entry(root)
                entry_3.insert(END,marks1[2])
                entry_3.grid(row = 8, column = 4, columnspan = 2)
                entry_4 = Entry(root)
                entry_4.insert(END,marks1[3])
                entry_4.grid(row = 10, column = 4, columnspan = 2)
                def success(e1g):
                    if marks2:
                        try:
                            self.cur.execute('''update marks 
                                set ia_1 = {}, ia_2 = {}, end_sem = {} where seat_no = '{}' 
                                and sub_id ='{}' '''.format(entry_2.get(),entry_3.get(),entry_4.get(),marks2[0],self.teacher[3]))
                        except Exception as e:
                            print(e)
                        self.conn.commit()
                        print('marks updated!')
                    else:
                        try:
                            seat = self.cur.execute('''select seat_no from student where roll_no = {}'''.format(e1g)).fetchone()
                            
                            self.cur.execute('''insert into marks 
                                values('{}',{},{},{},'{}') '''.format(seat[0],entry_2.get(),entry_3.get(),entry_4.get(),self.teacher[3]))
                        except Exception as e:
                            print(e,'errorc kr jej ej kef')
                        self.conn.commit()
                        print('marks updated2!')
                    time.sleep(1)
                    root.destroy()
                Button(root, text='Update',width=22,bg='brown',fg='white',command = lambda: success(e1g)).grid(row = 4, column = 3, rowspan = 2, stick = S, padx = 5, pady = 5)
                        
                
            
            
            
            
            Button(root, text='Fetch Data',width=22,bg='brown',fg='white',command =lambda: query1(entry_1.get())).grid(row = 4, column = 2, rowspan = 2, stick = S, padx = 5, pady = 5)
            Button(root, text='Cancel',width=22,bg='brown',fg='white',command = root.destroy).grid(row = 4, column = 5, rowspan = 2, stick = S, padx = 5, pady = 5)

            
                    

       

            
            
            
            
            
            
            
            
        
        for r in range(len(names)):
            self.query3 = '''select DISTINCT(marks.seat_no),roll_no,ia_1,ia_2,end_sem from Student,Marks WHERE marks.seat_no = Student.seat_no and marks.sub_id = '{}' and roll_no = '{}' '''.format(self.teacher[3],names[r][1])
            print(self.query3)
            marks = self.cur.execute(self.query3).fetchone()
            print(marks)
            #print(self.query3,marks)
            
            Label(root, text = '{} :- '.format(names[r][0]), borderwidth=3, font=("bold", 12), fg = 'red').grid(row = r+3, column = 0, columnspan = 2)
            if not marks:
                marks = ['nil','nil','nil','nil','nil']
                
            Label(root, text = '{}'.format(names[r][1]), borderwidth=3, font=("bold", 12), fg = 'red').grid(row = r+3, column = 2, columnspan = 2,padx = 5, pady = 5)
            Label(root, text = '{}'.format(marks[2]), borderwidth=3, font=("bold", 12), fg = 'red').grid(row = r+3, column = 4, columnspan = 2,padx = 5, pady = 5)            
            Label(root, text = '{}'.format(marks[3]), borderwidth=3, font=("bold", 12), fg = 'red').grid(row = r+3, column = 6, columnspan = 2,padx = 5, pady = 5)
            Label(root, text = '{}'.format(marks[4]), borderwidth=5, font=("bold", 12), fg = 'red').grid(row = r+3, column = 8, columnspan = 2,padx = 10, pady = 5)
            
        
        Button(root, text='Return to profile',width=22,bg='brown',fg='white',command = root.destroy).grid(row = len(names)+6, column = 1, rowspan = 2, stick = S, padx = 5, pady = 5)
        Button(root, text='Update Marks',width=22,bg='brown',fg='white',command = up).grid(row = len(names)+6, column = 4, rowspan = 2, stick = S, padx = 5, pady = 5)
        
        root.mainloop()
    
    def cgpa_predict(self):
        root = Tk()
        root.geometry('500x500')
        root.title("CGPA Predictor")
        root['bg'] = 'white'
        ##please include your file path for the icon here
        root.iconbitmap("Icons/4023873-brain-learning-machine-machine-learning-ml_112855.ico")
        
        title_pred = Label(root, text="CGPA Prediction",width=20,font=("bold", 20), bg = 'white')
        title_pred.place(x=90,y=53)
        
        body_1 = Label(root, text="Acc. to the model your predicted cgpa is : ",font=('bold', 10), bg = 'white')
        body_1.place(x=140,y=103)
        
        Button(root, text='Predict',width=22,bg='brown',fg='white').place(x=80,y=160)
        
        entry_pred = Entry(root)
        entry_pred.place(x=300,y=165,width = 140)
        
        body_2 = Label(root, text="**real life result may differ due to various factors",font=('italic', 8), bg = 'white')
        body_2.place(x=140,y=225)
        
        
        Button(root, text='Return to Profile',width=22,bg='brown',fg='white',command = root.destroy).place(x=150,y=300)
    
        
        root.mainloop()
    
    
    
    def pass_change(self):
    
        root = Tk()
        root.geometry('500x600')
        root.title("UPDATE PROFILE PASSWORD")
        root.iconbitmap("Icons/4023873-brain-learning-machine-machine-learning-ml_112855.ico")
    
        
        def pass_check():
            if entry_2.get()!=entry_3.get():
                print("Passwords dont match!!!!")
                Label(root,text="Passwords dont match! enter again!!!",font=("bold",12),fg= 'red').place(x=90,y=170)
            else: 
                salt = bcrypt.gensalt(10)
                if bcrypt.checkpw(entry_1.get().encode(),self.opass.encode()):
                    print("match")
                else:
                    print("does not match")
                    Label(root,text="Wrong Old password entered, try again!!!",font=("bold",12),fg= 'red').place(x=90,y=170)
                    return
                
                hashed1 = bcrypt.hashpw(entry_2.get().encode(), salt)
                
                try:
                    query  = "UPDATE Login_details set Password = '{}' where ID_no = '{}'".format(hashed1.decode(),self.teacher_id)
                    self.cur.execute(query)
                except Exception as e:
                    print(e)
        
                self.conn.commit()
                Label(root,text="Passwords successfully changed!!!",font=("bold",12),fg= 'red').place(x=90,y=170)
                time.sleep(1)
                root.destroy()
        
        label_0 = Label(root, text="{}'s Profile".format(self.teacher[0]),width=20,font=("bold", 20)).grid(row = 0,column = 3,columnspan = 3)
        
        
        
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
    
    
    def close_conn(self):
        self.conn.close()

#teacher_view1('loukik','1019149','4','COMPUTERS',1,2,'hello')

#s = teacher('101010','$2b$10$4arFcZWtWIYNQKwLHG.Xe.4ddaXNXGKZ126YkvEmWFDtlU1VUaXHi')
#s.main_view()
#s.close_conn()

