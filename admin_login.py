

import sqlite3
import tkinter  as tk 
from tkinter import *  
import time 
import numpy as np 
from tkinter import messagebox as ms

#import tkinter.messagebox

import os
from PIL import Image # For face recognition we will the the LBPH Face Recognizer 
from PIL import Image , ImageTk  

root = tk.Tk()
root.geometry('500x300')
root.title("Login Form")


Name=StringVar()
upass=StringVar()


#------------------------------------------------------

root.configure(background="seashell2")
#root.geometry("1300x700")
import sqlite3
my_conn = sqlite3.connect('face.db')

#w, h = root.winfo_screenwidth(), root.winfo_screenheight()
#root.geometry("%dx%d+0+0" % (w, h))


#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
# image2 =Image.open('bg1.jpg')
# image2 =image2.resize((500,300), Image.ANTIALIAS)

# background_image=ImageTk.PhotoImage(image2)

# background_label = tk.Label(root, image=background_image)

# background_label.image = background_image
# background_label.place(x=0, y=0)
# #-----------------------------------



# def login_now():
    
# ##### tkinter window ######
#     print("reg")
 
   
  
#     from subprocess import call
#     call(["python", "criminal_data.py"])  

def admin():
    user = Name.get()
    upass1 = upass.get()
    
    if (user == "Admin") & (upass1 == "admin"):    
       ms.showinfo("Success","Login Successfully !!")
       from subprocess import call
       call(["python", "add_cand.py"])
       
    else:
        ms.showinfo("error","Login Failed !!")


label_0 = Label(root, text="ADMIN LOGIN",width=20,font=("bold", 20))
label_0.place(x=90,y=53)



label_1 = Label(root, text="User Name",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=Name,bg="lightgray")
entry_1.place(x=300,y=130)

label_2 = Label(root, text="Password",width=20,font=("bold", 10))
label_2.place(x=80,y=180)

entry_2 = Entry(root,textvar=upass,show='*',bg="lightgray")
entry_2.place(x=300,y=180)

Button(root, text='Login Now',width=20,bg='brown',fg='white',command=admin).place(x=180,y=250)

 

root.mainloop()


