from tkinter import *
import customtkinter as ct
from PIL import Image, ImageTk
from database import Connect
from random import randint
from datetime import date

current_date = date.today()

db = Connect()

root = ct.CTk(fg_color="snow2")
main_frame = ct.CTkFrame(root, fg_color="snow2")
root.iconbitmap("C:/Users/chava/Desktop/csc project resources/Logo2.ico")
root.title("Outpatient booking")
root.geometry("1000x1000")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# background
img = Image.open("C:/Users/chava/Desktop/test.png")
bk = ct.CTkImage(dark_image=img, size=(1700, 1700))
lb = ct.CTkLabel(main_frame, image=bk, text="")
lb.place(relx=0, rely=0, relwidth=1, relheight=1)
lb.lower()

main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

# header
head = ct.CTkLabel(main_frame, text="Patient Details", text_color="Black", font=("Times New Roman", 80), bg_color="snow2")
head.place(x=550, y=50)

#options
option1 = ct.StringVar(value="[Select]")
option2 = ct.StringVar(value="[Select]")

#labels
condition = ct.CTkLabel(main_frame, text="Condition : ", text_color="Black", font=("TkinterDefaultFont", 30), bg_color="snow2")
doctor = ct.CTkLabel(main_frame, text = "Select doctor :",text_color = "Black",font = ("TkinterDefaultFont",30),bg_color = "snow2")
dept = ct.CTkLabel(main_frame, text = "Select department :",text_color = "Black",font = ("TkinterDefaultFont",30),bg_color = "snow2")
tno_label = ct.CTkLabel(main_frame, text = "Patient ID :",text_color = "Black",font = ("TkinterDefaultFont",30),bg_color = "snow2")

#entry widget
condition_entry = ct.CTkEntry(main_frame, width=300, placeholder_text="Enter condition", placeholder_text_color="Grey30", corner_radius=30, height=50, text_color="Black", fg_color=("purple3", "snow2"), justify="center", font=("TkDefaultFont", 20, "bold"), border_color="Midnight Blue", border_width=2)
tno_entry = ct.CTkEntry(main_frame, width=300, placeholder_text="Enter patient id", placeholder_text_color="Grey30", corner_radius=30, height=50, text_color="Black", fg_color=("purple3", "snow2"), justify="center", font=("TkDefaultFont", 20, "bold"), border_color="Midnight Blue", border_width=2)

#optionmenus
t = db.get_doctors()
l = ["-".join(tup) for tup in t ]
doctor_options = ct.CTkOptionMenu(main_frame, values = l,variable = option1,text_color = "Black",font = ("Inter",20),fg_color = "medium purple2",width = 150, height = 40,dropdown_hover_color = "Grey",button_color = "snow2",button_hover_color = "grey70")
dept_options = ct.CTkOptionMenu(main_frame, values = ["[Select]","Dermatology","Cardiology","Opthalmology","Dentistry"],variable = option2,text_color = "Black",fg_color = "medium purple2",width = 150, height = 40,font = ("Inter",20),dropdown_hover_color = "Grey",button_color = "snow2",button_hover_color = "grey70")


# placing widgets
condition.place(x = 300, y = 300)
condition_entry.place(x = 450, y = 295)
doctor.place(x = 900, y = 300)
doctor_options.place(x = 1100, y = 300)
dept.place(x = 300, y = 500)
dept_options.place(x = 570, y = 500)
tno_label.place(x = 900, y = 500)
tno_entry.place(x = 1055, y = 495)

def restore_ui():
    global error,back_btn,option1,option2,condition_entry,doctor_options,dept_options,tno_entry
    name,phone,email,condition,dob = ""
    if back_btn:
        back_btn.destroy()
        back_btn = None
    if error:
        error.destroy()
        error = None
    
    #widgets
    head = ct.CTkLabel(main_frame, text = "Book a room",text_color = "Black",font=("TkinterDefaultFont",80),bg_color="snow2")
    head.place(x = 580, y = 50)
    
    #labels
    condition = ct.CTkLabel(main_frame, text="Condition : ", text_color="Black", font=("TkinterDefaultFont", 30), bg_color="snow2")
    doctor = ct.CTkLabel(main_frame, text = "Select doctor :",text_color = "Black",font = ("TkinterDefaultFont",30),bg_color = "snow2")
    dept = ct.CTkLabel(main_frame, text = "Select department :",text_color = "Black",font = ("TkinterDefaultFont",30),bg_color = "snow2")
    tno_label = ct.CTkLabel(main_frame, text = "Patient ID :",text_color = "Black",font = ("TkinterDefaultFont",30),bg_color = "snow2")
    
    #entry widget
    condition_entry = ct.CTkEntry(main_frame, width=300, placeholder_text="Enter condition", placeholder_text_color="Grey30", corner_radius=30, height=50, text_color="Black", fg_color=("purple3", "snow2"), justify="center", font=("TkDefaultFont", 20, "bold"), border_color="Midnight Blue", border_width=2)
    tno_entry = ct.CTkEntry(main_frame, width=300, placeholder_text="Enter patient id", placeholder_text_color="Grey30", corner_radius=30, height=50, text_color="Black", fg_color=("purple3", "snow2"), justify="center", font=("TkDefaultFont", 20, "bold"), border_color="Midnight Blue", border_width=2)
    
    #optionmenus
    doctor_options = ct.CTkOptionMenu(main_frame, values = l,variable = option1,text_color = "Black",font = ("Inter",20),fg_color = "medium purple2",width = 150, height = 40,dropdown_hover_color = "Grey",button_color = "snow2",button_hover_color = "grey70")
    dept_options = ct.CTkOptionMenu(main_frame, values = ["[Select]","Dermatology","Cardiology","Opthalmology","Dentistry"],variable = option2,text_color = "Black",fg_color = "medium purple2",width = 150, height = 40,font = ("Inter",20),dropdown_hover_color = "Grey",button_color = "snow2",button_hover_color = "grey70")

    #placement
    condition.place(x = 300, y = 300)
    condition_entry.place(x = 450, y = 295)
    doctor.place(x = 900, y = 300)
    doctor_options.place(x = 1100, y = 300)
    dept.place(x = 300, y = 500)
    dept_options.place(x = 570, y = 500)
    tno_label.place(x = 900, y = 500)
    tno_entry.place(x = 1055, y = 495)
    
    #buttons
    register = ct.CTkButton(main_frame, text="Feed",width=200, command = getval,text_color="Black", corner_radius=50,height=60, fg_color=("purple", "White"), font=ct.CTkFont("TkDefaultFont", 17, "bold"),border_color="Midnight Blue", border_width=2, hover_color="purple3")
    register.place(x=700, y=700)
        
def getval():
    global error,back_btn,condition_val,doc_val,dept_val,tno_val
    condition_val = condition_entry.get()
    doc_val = option1.get()
    dept_val = option2.get()
    tno_val = int(tno_entry.get())
    
    if (condition_val.strip() not in ("","Enter condition") and doc_val!="[Select]" and dept_val!="[Select]" and tno_val!=""):
        if int(tno_val) in db.get_outpatient_ids():
            db.update_outpatient_self(doc_val,condition_val,dept_val,int(tno_val))
            success_label = ct.CTkLabel(main_frame, text="Details confirmed!", text_color="green", font=("TkDefaultFont", 25, "bold"), bg_color="snow2")
            success_label.place(x=680, y=770)
        else:
            error = ct.CTkLabel(main_frame, text="No such id exists!", text_color="red", font=("TkDefaultFont", 25, "bold"), bg_color="snow2")
            error.place(x=680, y=770)
            
    else:
        for widget in main_frame.winfo_children():
            if widget != lb:
                widget.destroy()
        error = ct.CTkLabel(main_frame, text = "Please fill all fields",text_color = "Black",font=("room_conds New Roman",80),bg_color="snow2")
        error.place(x = 450, y = 300)
        back_btn = ct.CTkButton(main_frame, text="Back", command=restore_ui,text_color="Black", corner_radius=30, height=60,fg_color=("purple", "White"), font=ct.CTkFont("TkDefaultFont", 17, "bold"),border_color="Midnight Blue", border_width=2, hover_color="purple3")
        back_btn.place(relx=0.45, rely=0.9)


#button
register = ct.CTkButton(main_frame, text="Feed",width=200, command = getval,text_color="Black", corner_radius=50,height=60, fg_color=("purple", "White"), font=ct.CTkFont("TkDefaultFont", 17, "bold"),border_color="Midnight Blue", border_width=2, hover_color="purple3")
register.place(x=700, y=700)

root.mainloop()