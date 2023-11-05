import tkinter as tk
from tkinter import ttk, LEFT, END
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re


##############################################+=============================================================
root = tk.Tk()
root.configure(background="black")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("700x650+200+100")
root.title("Login Form")




voter_id = tk.StringVar()
password = tk.StringVar()
        

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('b.jpg')
image2 = image2.resize((w,h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)



# CREATE TABLE "user_reg" (
# 	"id"	INTEGER,
# 	"Fullname"	TEXT,
# 	"Adhar_No"	INTEGER,
# 	"Voter_ID"	TEXT,
# 	"Password"	TEXT,
# 	"Phone_No"	INTEGER,
# 	"Email_id"	TEXT,
# 	"status"	TEXT,
# 	PRIMARY KEY("id" AUTOINCREMENT)
# );


def registration():
    from subprocess import call
    call(["python","register.py"])
    root.destroy()

def login():
        # Establish Connection

    with sqlite3.connect('evaluation.db') as db:
         c = db.cursor()

        # Find user If there is any take proper action
         db = sqlite3.connect('evaluation.db')
         cursor = db.cursor()
         cursor.execute("CREATE TABLE IF NOT EXISTS user_reg "
                            "(id	INTEGER, Fullname TEXT, Adhar_No INTEGER, Voter_ID TEXT, Password TEXT,Phone_No INTEGER,Email_id TEXT , status TEXT)")
         db.commit()
         find_entry = ('SELECT * FROM user_reg WHERE Voter_ID = ? and Password = ?')
         c.execute(find_entry, [(voter_id.get()), (password.get())])
         result = c.fetchall()

         if result:
            msg = ""
            # self.logf.pack_forget()
            # self.head['text'] = self.username.get() + '\n Loged In'
            # msg = self.head['text']
            #            self.head['pady'] = 150
            print(msg)
            ms.showinfo("messege", "LogIn sucessfully")
            # ===========================================
            root.destroy()

            from subprocess import call
            call(['python','GUI_R_V.py'])

            # ================================================
         else:
           ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')


# frame_alpr = tk.LabelFrame(root, text=" --About us-- ", width=550, height=500, bd=5, font=('times', 14, ' bold '),bg="#7CCD7C")
# frame_alpr.grid(row=0, column=0, sticky='nw')
# frame_alpr.place(x=550, y=200)

# label_l2 = tk.Label(root, text="___ Login Form ___",font=("Times New Roman", 30, 'bold'),
#                     background="#EEEE00", fg="black", width=67, height=3)
# label_l2.place(x=0, y=90)


#bg1_icon=ImageTk.PhotoImage(file="E:\\30%-phising-attack\\b2.png")

bg_icon=ImageTk.PhotoImage(file="D:/new/Smart_Voting_System/L.jpg")
user_icon=ImageTk.PhotoImage(file="D:/new/Smart_Voting_System/l1.png")
pass_icon=ImageTk.PhotoImage(file="D:/new/Smart_Voting_System/p1.jpg")
        
# bg_lbl=tk.Label(root,image=bg1_icon, width=600,height=600)
# bg_lbl.place(x=50,y=50)
        
title=tk.Label(root, text="Login Here", font=("Algerian", 30, "bold","italic"),bd=5,bg="black",fg="white")
title.place(x=220,y=100,width=250)
        
Login_frame=tk.Frame(root,bg="white")
Login_frame.place(x=100,y=250)
        
logolbl=tk.Label(Login_frame,image=bg_icon,bd=0).grid(row=0,columnspan=2,pady=20)
        
lbluser=tk.Label(Login_frame,text="Voter_ID",image=user_icon,compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
txtuser=tk.Entry(Login_frame,bd=5,textvariable=voter_id,font=("",15))
txtuser.grid(row=1,column=1,padx=20)
        
lblpass=tk.Label(Login_frame,text="Password",image=pass_icon,compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").grid(row=2,column=0,padx=50,pady=10)
txtpass=tk.Entry(Login_frame,bd=5,textvariable=password,show="*",font=("",15))
txtpass.grid(row=2,column=1,padx=20)
        
btn_log=tk.Button(Login_frame,text="Login",command=login,width=15,font=("Times new roman", 14, "bold"),bg="brown",fg="white")
btn_log.grid(row=3,column=1,pady=10)
btn_reg=tk.Button(Login_frame,text="Create Account",command=registration,width=15,font=("Times new roman", 14, "bold"),bg="black",fg="white")
btn_reg.grid(row=3,column=0,pady=10)
        
        
    
       
        # Login Function       





root.mainloop()