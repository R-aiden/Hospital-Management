from tkinter import *
import customtkinter as ct
from PIL import Image,ImageTk
import subprocess
from database import Connect

db = Connect()

root = ct.CTk(fg_color="snow2")
root.iconbitmap("C:/Users\chava\Desktop\csc project resources/Logo2.ico")
root.title("Login Page")
root.geometry("750x750")
root.grid_rowconfigure(0,weight = 1)
root.grid_columnconfigure(0,weight = 1)

#background
img = Image.open("C:/Users/chava/Desktop/test.png")
bk = ct.CTkImage(dark_image=img,size = (1700,1700))
lb = ct.CTkLabel(root,image=bk,text="")
lb.place(relx=0, rely=0, relwidth=1, relheight=1)
lb.lower()

#header
gt = ct.CTkLabel(root,text = "Welcome",font=("Times New Roman",100),text_color = "Black",bg_color = "grey93",anchor = CENTER)
logo = Image.open("C:/Users/chava/Desktop/csc project resources/Logo2.jpg")
bk2 = ct.CTkImage(dark_image=logo, size = (200,200))
imlb = ct.CTkLabel(root,image=bk2,text="")
gt.place(x = 200, y = 250)
imlb.place(x = 300, y = 400)


#heading
ft2 = ct.CTkFont(family = "Playfair Display",size = 80)
desc = ct.CTkLabel(root, text = "Please enter your credentials to continue",text_color="Black",font=("TkDefaultFont",20),bg_color = "snow2")
head = ct.CTkLabel(root, text = "LOGIN",text_color = "Black",font=ft2,bg_color="snow2")
head.grid(row = 0, column = 1, sticky = "n",padx = 300, pady = 90)
desc.grid(row = 0, column = 1,sticky = "n",padx = 100, pady =200)

#error
error = ct.CTkLabel(root, text="", text_color="red", font=("TkDefaultFont", 25, "bold"), bg_color="snow2")
error.place(x = 1013, y = 750)

#login functions
def login_commands():
    def getval():    
        user = u.get()
        password = p.get()
        information = [user,password]
        if user!="" and password!="":
            print(information)
    def checks():
        global error
        user = u.get()
        password = p.get()
        error.configure(text = "")
        if check.get()=="Doctor":
            if password.strip() == db.get_login_doc(user):
                subprocess.Popen(["python","C:/Users/chava/Desktop/Hospital Management/Doctor Dashboard.py",u.get()])
            else:
               error.configure(text = "Please enter correct password!")
               
        elif check.get()=="Nurse":
            #print(f"Entered: '{password}' | From DB: '{db.get_login_nurse(user)}'")
            if password.strip() == db.get_login_nurse(user):
                subprocess.Popen(["python","C:/Users/chava/Desktop/Hospital Management/Nurse Dashboard.py",u.get()])
            else:
               error.configure(text = "Please enter correct password!")
               
        elif check.get()=="Admin":
            if password.strip() == db.get_login_admin(user):
                subprocess.Popen(["python","C:/Users/chava/Desktop/Hospital Management/Admin Dashboard.py",u.get()])
            else:
                error.configure(text = "Please enter correct password!")
                
    getval()
    checks()

#entry and login button
u = ct.CTkEntry(root,width = 300,placeholder_text = "Enter Username",placeholder_text_color = "Grey30",corner_radius=30,height = 50,text_color = "Black",fg_color = ("purple3","snow2"),justify = "center",font=("TkDefaultFont",20,"bold"),border_color = "Midnight Blue",border_width = 2)
p = ct.CTkEntry(root,width = 300,corner_radius=30,height = 50,placeholder_text = "Enter Password",placeholder_text_color = "Grey30",text_color = "Black",fg_color = ("purple","snow2"),justify = "center",font=("TkDefaultFont",20,"bold"),border_color ="Midnight Blue",border_width = 2)
e = ct.CTkButton(root,text = "Login",width = 200,command = login_commands,text_color = "Black",corner_radius = 50,height = 60,fg_color = ("purple","snow2"),font=ct.CTkFont("TkDefaultFont",17,"bold"),border_color = "Midnight Blue",border_width = 2,hover_color = "purple3")
e.place(x=1013, y = 500)
u.place(x=960, y = 300)
p.place(x=960, y = 400)

check = ct.StringVar(value="")

#tickboxes
d = ct.CTkRadioButton(root,text = "Doctor",variable = check,value = "Doctor",hover_color = "purple",text_color = "Black",font=("TkDefaultFont",20,"bold"))
n = ct.CTkRadioButton(root,text = "Nurse",variable = check,value = "Nurse",hover_color= "purple",text_color = "Black",font=("TkDefaultFont",20,"bold"))
a = ct.CTkRadioButton(root,text = "Admin",variable = check,value = "Admin",hover_color= "purple",text_color = "Black",font=("TkDefaultFont",20,"bold"))
d.place(x = 1013,y = 600)
n.place(x = 1013,y = 650)
a.place(x = 1012,y = 700)



root.mainloop()