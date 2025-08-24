from tkinter import *
import customtkinter as ct
from PIL import Image
import subprocess

#print("Opened main menu.py")
root = ct.CTk(fg_color="snow2")
root.iconbitmap(r"C:\Users\chava\Desktop\csc project resources\altlogo.ico")
root.title("Main menu")
root.geometry("1000x1000")
root.grid_rowconfigure(0,weight = 1)
root.grid_columnconfigure(0,weight = 1)
head = ct.CTkLabel(root, text = "Main Menu",text_color = "Black",font=("Times New Roman",80),bg_color="snow2")
head.grid(row = 0, column = 0,columnspan = 2, sticky = "n",padx = 200, pady = 50)

#background
img = Image.open(r"C:\Users\chava\Desktop\test.png")
bk = ct.CTkImage(dark_image=img,size = (1700,1700))
lb = ct.CTkLabel(root,image=bk,text="")
lb.place(relx=0, rely=0, relwidth=1, relheight=1)
lb.lower()


#prompt for other windows
def login_page():
    subprocess.Popen(["python",r"C:\Users\chava\Desktop\Hospital Management\Login.py"])
    
def booking_page():
    subprocess.Popen(["python",r"C:\Users\chava\Desktop\Hospital Management\PatientBooking.py"])
    
def billing_page():
    subprocess.Popen(["python",r"C:\Users\chava\Desktop\Hospital Management\BillingAction.py"])
    
def employ_regis():
    subprocess.Popen(["python",r"C:\Users\chava\Desktop\Hospital Management\Employee Registration.py"])

#menu
login = ct.CTkButton(root, text = "Login Page",width = 400, height = 50,corner_radius = 50,text_color = "Black",fg_color = "purple1",font = ("Intel",20,"bold"),hover_color = "purple3",command = login_page)
billing = ct.CTkButton(root, text = "Billing Page",width = 400, height = 50,corner_radius = 50,text_color = "Black",fg_color = "purple1",font = ("Intel",20,"bold"),hover_color = "purple3",command = billing_page)
booking = ct.CTkButton(root, text = "Book an appointment",width = 400, height = 50,corner_radius = 50,text_color = "Black",fg_color = "purple1",font = ("Intel",20,"bold"),hover_color = "purple3",command = booking_page)
employ_reg = ct.CTkButton(root, text = "Register as an employee",width = 400, height = 50,corner_radius = 50,text_color = "Black",fg_color = "purple1",font = ("Intel",20,"bold"),hover_color = "purple3",command = employ_regis)

#placement
login.place(x = 575, y = 300)
booking.place(x = 575, y= 400)
billing.place(x = 575, y = 500)
employ_reg.place(x = 575, y = 600)

root.mainloop()