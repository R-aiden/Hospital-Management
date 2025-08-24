from tkinter import *
import customtkinter as ct
from PIL import Image,ImageTk
import subprocess
from database import Connect
import sys

db = Connect()

root = ct.CTk(fg_color="snow2")
root.iconbitmap("C:/Users\chava\Desktop\csc project resources/Logo2.ico")
root.title("Dashboard")
root.geometry("1000x1000")
root.grid_rowconfigure(0,weight = 1)
root.grid_columnconfigure(0,weight = 1)

sidebar_color = "#f4edfc"
button_color = "#e3d5f9"
hover_color = "#f0e9fd"

username = sys.argv[1]
doctor_data = db.retrieve_doctor(username)
    
if doctor_data is None:
    name_doc = ""
else:
    name_doc = doctor_data[1]

#frame for sidebar
container = ct.CTkFrame(root, fg_color="snow2")
container.pack(fill="both", expand=True)

welcome_lable = ct.CTkLabel(root, text = "Welcome Dr.{}!".format(name_doc),text_color = "Black",font=("TkinterDefaultFont",80),bg_color="snow2")
welcome_lable.place(x = 500, y = 300)

#Sidebar
sidebar = ct.CTkFrame(container, width=240, fg_color=sidebar_color, corner_radius=15)
sidebar.pack(side="left", fill="y", padx=10, pady=50)

#Heading
heading = ct.CTkLabel(sidebar, text="Dashboard", text_color="black", font=ct.CTkFont(size=22, weight="bold"))
heading.pack(pady=(25, 20))

def show():
    welcome_lable.destroy()
    print("show")
    if doctor_data:
        e_id_val,name_val,field_val,salary_val,dob_val,phone_val,email_val,gender_val,user_id,pass_id = doctor_data
        
        name = ct.CTkLabel(root, text=f"Name : {name_val}", text_color="Black", font=("TkinterDefaultFont", 30), bg_color="snow2")
        field_val = ct.CTkLabel(root, text=f"Field : {field_val}", text_color="Black", font=("TkinterDefaultFont", 30), bg_color="snow2")
        salary = ct.CTkLabel(root, text=f"Salary : {salary_val}", text_color="Black", font=("TkinterDefaultFont", 30), bg_color="snow2")
        phone_no = ct.CTkLabel(root, text=f"Phone No : {phone_val}", text_color="Black", font=("TkinterDefaultFont", 30), bg_color="snow2")
        email = ct.CTkLabel(root, text=f"Email : {email_val}", text_color="Black", font=("TkinterDefaultFont", 30), bg_color="snow2")
        dob = ct.CTkLabel(root, text=f"DOB : {dob_val}", text_color="Black", font=("TkinterDefaultFont", 30), bg_color="snow2")
        e_id = ct.CTkLabel(root, text=f"Employee Id : {e_id_val}", text_color="Black", font=("TkinterDefaultFont", 30), bg_color="snow2")
        gender = ct.CTkLabel(root, text=f"Gender : {gender_val}", text_color="Black", font=("TkinterDefaultFont", 30), bg_color="snow2")
        user = ct.CTkLabel(root, text=f"Username : {user_id}", text_color="Black", font=("TkinterDefaultFont", 30), bg_color="snow2")
        password = ct.CTkLabel(root, text=f"Password : {pass_id}", text_color="Black", font=("TkinterDefaultFont", 30), bg_color="snow2")
        
        name.place(x=500, y=100)
        salary.place(x=1000, y=100)
        field_val.place(x = 1000 , y = 400)
        phone_no.place(x=500, y=250)
        email.place(x=1000, y=250)
        dob.place(x=500, y=400)
        e_id.place(x=500, y=550)
        gender.place(x=1000, y=550)
        user.place(x = 500, y = 700)
        password.place(x = 1000, y = 700)
        
#buttons
btn_details = ct.CTkButton(sidebar, text="Details", text_color="black", command = show,fg_color=button_color, hover_color=hover_color, corner_radius=10, font=ct.CTkFont(size=17))
btn_details.pack(pady=15, padx=20, fill="x")

root.mainloop()


