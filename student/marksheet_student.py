# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 17:27:09 2021

@author: LOUKIK RAINA
"""

from tkinter import *

def student_view1(pre,sub):

    root = Tk()
    #root.geometry('600x700')
    root.title("STUDENT PROFILE")
    root.iconbitmap("./4023873-brain-learning-machine-machine-learning-ml_112855.ico")

    
    
    label_0 = Label(root, text="{}'s Marksheet".format('Loukik'),width=20,font=("bold", 20)).grid(row = 0,column = 1,columnspan = 3,rowspan = 2)
       
    Label(root, text = 'SUBJECTS', borderwidth=3, font=("bold", 14), fg = 'green',bg = 'yellow').grid(row = 2, column = 0, columnspan = 2)
    Label(root, text = 'IA 1', borderwidth=3, font=("bold", 14), fg = 'green',bg = 'yellow').grid(row = 2, column = 2, columnspan = 2)
    Label(root, text = 'IA 2', borderwidth=3, font=("bold", 14), fg = 'green',bg = 'yellow').grid(row = 2, column = 4, columnspan = 2)
    Label(root, text = 'ENDSEM', borderwidth=3, font=("bold", 14), fg = 'green',bg = 'yellow').grid(row = 2, column = 6, columnspan = 2)

    
    for r in range(sub):
        Label(root, text = '{} :- '.format(r), borderwidth=3, font=("bold", 12), fg = 'red').grid(row = r+3, column = 0, columnspan = 2)
        Label(root, text = 'answer ia1 {}'.format(r), borderwidth=3, font=("bold", 12), fg = 'red').grid(row = r+3, column = 2, columnspan = 2,padx = 5, pady = 5)
        Label(root, text = 'answer ia2{}'.format(r), borderwidth=3, font=("bold", 12), fg = 'red').grid(row = r+3, column = 4, columnspan = 2,padx = 5, pady = 5)
        Label(root, text = 'answer endsem{}'.format(r), borderwidth=5, font=("bold", 12), fg = 'red').grid(row = r+3, column = 6, columnspan = 2,padx = 10, pady = 5)
    
    
    Button(root, text='Return to profile',width=22,bg='brown',fg='white',command = root.destroy).grid(row = sub+6, column = 1, rowspan = 2, stick = S, padx = 5, pady = 5)
    Button(root, text='Predict',width=22,bg='brown',fg='white',command = pre).grid(row = sub+6, column = 4, rowspan = 2, stick = S, padx = 5, pady = 5)
    
    root.mainloop()
    
