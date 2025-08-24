from tkinter import *
import customtkinter as ct
from PIL import Image,ImageTk
import subprocess
from database import Connect
import sys

db = Connect()

#main window
root = ct.CTk(fg_color="snow2")
global main_frame
main_frame = ct.CTkFrame(root,fg_color = "transparent")
root.iconbitmap("C:/Users\chava\Desktop\csc project resources/Logo2.ico")
root.title("Admin Dashboard")
root.geometry("1000x1000")
root.grid_rowconfigure(0,weight = 1)
root.grid_columnconfigure(0,weight = 1)

main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)


username = sys.argv[1]
admin_data = db.retrieve_admin(username)

if admin_data is None:
    name = ""
else:
    name = admin_data[1]
    
welcome_lable = ct.CTkLabel(main_frame, text = "Welcome {}!".format(name),text_color = "Black",font=("TkinterDefaultFont",80),bg_color="snow2")
welcome_lable.place(x = 500, y = 300)

def show():
    welcome_lable.destroy()
    if admin_data:
        e_id_val, name_val, salary_val, dob_val, phone_val, gender_val, email_val,user_id,pass_id = admin_data

        name = ct.CTkLabel(main_frame, text=f"Name : {name_val}", text_color="Black", font=("TkinterDefaultFont", 30), bg_color="snow2")
        salary = ct.CTkLabel(main_frame, text=f"Salary : {salary_val}", text_color="Black", font=("TkinterDefaultFont", 30), bg_color="snow2")
        phone_no = ct.CTkLabel(main_frame, text=f"Phone No : {phone_val}", text_color="Black", font=("TkinterDefaultFont", 30), bg_color="snow2")
        email = ct.CTkLabel(main_frame, text=f"Email : {email_val}", text_color="Black", font=("TkinterDefaultFont", 30), bg_color="snow2")
        dob = ct.CTkLabel(main_frame, text=f"DOB : {dob_val}", text_color="Black", font=("TkinterDefaultFont", 30), bg_color="snow2")
        e_id = ct.CTkLabel(main_frame, text=f"Employee Id : {e_id_val}", text_color="Black", font=("TkinterDefaultFont", 30), bg_color="snow2")
        gender = ct.CTkLabel(main_frame, text=f"Gender : {gender_val}", text_color="Black", font=("TkinterDefaultFont", 30), bg_color="snow2")
        user = ct.CTkLabel(main_frame, text=f"Username : {user_id}", text_color="Black", font=("TkinterDefaultFont", 30), bg_color="snow2")
        password = ct.CTkLabel(main_frame, text=f"Password : {pass_id}", text_color="Black", font=("TkinterDefaultFont", 30), bg_color="snow2")
        
        name.place(x=500, y=100)
        salary.place(x=1000, y=100)
        phone_no.place(x=500, y=250)
        email.place(x=1000, y=250)
        dob.place(x=500, y=400)
        e_id.place(x=500, y=550)
        gender.place(x=1000, y=550)
        user.place(x = 500, y = 700)
        password.place(x = 1000, y = 700)

def action():
    subprocess.Popen(["python","C:/Users/chava/Desktop/Hospital Management/Patient Registration.py"])

sidebar_color = "#f4eeee"
button_color = "#d9c7f1"
hover_color = "#e9defa"

#Sidebar
sidebar = ct.CTkFrame(main_frame, width=240, fg_color=sidebar_color, corner_radius=15)
sidebar.pack(side="left", fill="y", padx=10, pady=50)

#Heading
heading = ct.CTkLabel(sidebar, text="Dashboard", text_color="black", font=ct.CTkFont(size=22, weight="bold"))
heading.pack(pady=(25, 20))	

#buttons
details = ct.CTkButton(sidebar, text="Details", command = show,text_color="black", fg_color=button_color, hover_color=hover_color, corner_radius=10, font=ct.CTkFont(size=17))
details.pack(pady=15, padx=20, fill="x")

schedule = ct.CTkButton(sidebar, text="Register Patients", command = action,text_color="black", fg_color=button_color, hover_color=hover_color, corner_radius=10, font=ct.CTkFont(size=17))
schedule.pack(pady=10, padx=20, fill="x")


root.mainloop()

