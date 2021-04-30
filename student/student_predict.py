from tkinter import *
import sqlite3
import sys

def cgpa_predict():
    root = Tk()
    root.geometry('500x500')
    root.title("CGPA Predictor")
    root['bg'] = 'white'
    ##please include your file path for the icon here
    root.iconbitmap("./4023873-brain-learning-machine-machine-learning-ml_112855.ico")
    
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
cgpa_predict()