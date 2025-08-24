from tkinter import *
import customtkinter as ct
from PIL import Image, ImageTk
from database import Connect
from random import randint
from datetime import date

now = date.today()

db = Connect()

root = ct.CTk(fg_color="snow2")
main_frame = ct.CTkFrame(root, fg_color="snow2")
root.iconbitmap(r"C:/Users/chava/Desktop/csc project resources/Logo2.ico")
root.title("Patient Registration")
root.geometry("1000x1000")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# background
img = Image.open(r"C:/Users/chava/Desktop/test.png")
main_frame.bk = ct.CTkImage(dark_image=img, size=(1700, 1700))
main_frame.lb = ct.CTkLabel(main_frame, image=main_frame.bk, text="")
main_frame.lb.place(relx=0, rely=0, relwidth=1, relheight=1)
main_frame.lb.lower()

main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

# variables
option1 = ct.StringVar(value="[Select]")
option2 = ct.StringVar(value="[Select]")
error = None
back_btn = None

#labels
gender_label = ct.CTkLabel(main_frame, text="Gender : ", text_color="Black", font=("TkinterDefaultFont", 30), bg_color="snow2")
type_of_patient_label = ct.CTkLabel(main_frame, text="Patient Type : ", text_color="Black", font=("TkinterDefaultFont", 30), bg_color="snow2")
p_id = ct.CTkLabel(main_frame, text="Patient ID : ", text_color="Black", font=("TkinterDefaultFont", 30), bg_color="snow2")
condition_label = ct.CTkLabel(main_frame, text="Patient Condition", text_color="Black", font=("TkinterDefaultFont", 27), bg_color="snow2")

# entry widgets
name = ct.CTkEntry(main_frame, width=300, placeholder_text="Enter name", placeholder_text_color="Grey30", corner_radius=30, height=50, text_color="Black", fg_color=("purple3", "snow2"), justify="center", font=("TkDefaultFont", 20, "bold"), border_color="Midnight Blue", border_width=2)
gender = ct.CTkOptionMenu(main_frame, values=["[Select]", "Male", "Female"], variable=option1, text_color="Black",fg_color="medium purple2", width=150, height=40, font=("Inter", 20), dropdown_hover_color="Grey",button_color="snow2", button_hover_color="grey70")
phone = ct.CTkEntry(main_frame, width=300, placeholder_text="Enter phone number", placeholder_text_color="Grey30", corner_radius=30,height=50, text_color="Black", fg_color=("purple3", "snow2"), justify="center", font=("TkDefaultFont", 20, "bold"),border_color="Midnight Blue", border_width=2)
condition = ct.CTkEntry(main_frame, width=300,placeholder_text="Enter past condition",placeholder_text_color="Grey30", state = "disabled",corner_radius=30,height=50, text_color="Black", fg_color=("purple3", "snow2"), justify="center", font=("TkDefaultFont", 20, "bold"),border_color="Midnight Blue", border_width=2)
email = ct.CTkEntry(main_frame, width=300, corner_radius=30, placeholder_text="Enter email", placeholder_text_color="Grey30",height=50, text_color="Black", fg_color=("purple3", "snow2"), justify="center", font=("TkDefaultFont", 20, "bold"),border_color="Midnight Blue", border_width=2)
dob = ct.CTkEntry(main_frame, width=300, corner_radius=30, placeholder_text="Enter DOB(DDMMYYYY)", placeholder_text_color="Grey30",height=50, text_color="Black", fg_color=("purple3", "snow2"), justify="center", font=("TkDefaultFont", 20, "bold"),border_color="Midnight Blue", border_width=2)

#optionpanel
type_of_patient = ct.CTkOptionMenu(main_frame, values=["[Select]", "In Patient", "Out Patient"], variable=option2, text_color="Black",fg_color="medium purple2", width=150, height=40, font=("Inter", 20), dropdown_hover_color="Grey",button_color="snow2", button_hover_color="grey70")


# placing widgets
name.place(x=170, y=300)
dob.place(x=1100, y=300)
gender_label.place(x=200, y=450)
gender.place(x=350, y=450)
phone.place(x=650, y=450)
email.place(x=1100, y=450)
type_of_patient_label.place(x = 600, y = 310)
type_of_patient.place(x = 800, y = 310)
condition.place(x = 1100, y = 600)
condition_label.place(x = 1150, y = 650)
p_id.place(x = 200, y = 600)

# header
head = ct.CTkLabel(main_frame, text="Patient Registration", text_color="Black", font=("Times New Roman", 80), bg_color="snow2")
head.place(x=475, y=50)

#to restore ui
def restore_ui():
    global error, back_btn, name, dob, gender, email, option1,option2,phone,condition,main_frame

    # Remove error and back button
    if back_btn:
        back_btn.destroy()
        back_btn = None
    if error:
        error.destroy()
        error = None
        
    head = ct.CTkLabel(main_frame, text="Patient Registration", text_color="Black",font=("Times New Roman", 80), bg_color="snow2")               
    head.place(x=475, y=50)

    # Reset dropdown option
    option1.set("[Select]")
    option2.set("[Select]")

    # Destroy existing input widgets
    for widget in [name, condition, dob, email, gender, phone]:
        if widget:
            widget.destroy()
            
    main_frame.lb = ct.CTkLabel(main_frame, image=main_frame.bk, text="")
    main_frame.lb.place(relx=0, rely=0, relwidth=1, relheight=1)
    main_frame.lb.lower()

    # Recreate entry widgets
    name = ct.CTkEntry(main_frame, width=300, placeholder_text="Enter name", placeholder_text_color="Grey30", corner_radius=30, height=50, text_color="Black", fg_color=("purple3", "snow2"), justify="center", font=("TkDefaultFont", 20, "bold"), border_color="Midnight Blue", border_width=2)
    gender_label = ct.CTkLabel(main_frame, text="Gender : ", text_color="Black", font=("TkinterDefaultFont", 30), bg_color="snow2")
    gender = ct.CTkOptionMenu(main_frame, values=["[Select]", "Male", "Female"], variable=option1, text_color="Black",fg_color="medium purple2", width=150, height=40, font=("Inter", 20), dropdown_hover_color="Grey",button_color="snow2", button_hover_color="grey70")
    phone = ct.CTkEntry(main_frame, width=300, placeholder_text="Enter phone number", placeholder_text_color="Grey30", corner_radius=30,height=50, text_color="Black", fg_color=("purple3", "snow2"), justify="center", font=("TkDefaultFont", 20, "bold"),border_color="Midnight Blue", border_width=2)
    condition = ct.CTkEntry(main_frame, width=300, state = "disabled",placeholder_text="Enter condition", placeholder_text_color="Grey30", corner_radius=30,height=50, text_color="Black", fg_color=("purple3", "snow2"), justify="center", font=("TkDefaultFont", 20, "bold"),border_color="Midnight Blue", border_width=2)
    email = ct.CTkEntry(main_frame, width=300, corner_radius=30, placeholder_text="Enter email", placeholder_text_color="Grey30",height=50, text_color="Black", fg_color=("purple3", "snow2"), justify="center", font=("TkDefaultFont", 20, "bold"),border_color="Midnight Blue", border_width=2)
    dob = ct.CTkEntry(main_frame, width=300, corner_radius=30, placeholder_text="Enter DOB\nYY/MM/DD", placeholder_text_color="Grey30",height=50, text_color="Black", fg_color=("purple3", "snow2"), justify="center", font=("TkDefaultFont", 20, "bold"),border_color="Midnight Blue", border_width=2)
    type_of_patient_label = ct.CTkLabel(main_frame, text="Patient Type : ", text_color="Black", font=("TkinterDefaultFont", 30), bg_color="snow2")
    type_of_patient = ct.CTkOptionMenu(main_frame, values=["[Select]", "In Patient", "Out Patient"], variable=option2, text_color="Black",fg_color="medium purple2", width=150, height=40, font=("Inter", 20), dropdown_hover_color="Grey",button_color="snow2", button_hover_color="grey70")
    p_id = ct.CTkLabel(main_frame, text="Patient ID : ", text_color="Black", font=("TkinterDefaultFont", 30), bg_color="snow2")
    
    name.place(x=170, y=300)
    dob.place(x=1100, y=300)
    gender_label.place(x=200, y=450)
    gender.place(x=350, y=450)
    phone.place(x=650, y=450)
    email.place(x=1100, y=450)
    type_of_patient_label.place(x = 600, y = 310)
    type_of_patient.place(x = 800, y = 310)
    condition.place(x = 1100, y = 600)
    condition_label.place(x = 1150, y = 650)
    p_id.place(x = 200, y = 600)

    # Buttons
    register = ct.CTkButton(main_frame, text="Register", command=getval1, width=200,text_color="Black", corner_radius=50, height=60,fg_color=("purple", "White"),font=ct.CTkFont("TkDefaultFont", 17, "bold"),border_color="Midnight Blue", border_width=2, hover_color="purple3")
    update = ct.CTkButton(main_frame, text="Update", command=getval2, width=200,text_color="Black", corner_radius=50, height=60,fg_color=("purple", "White"),font=ct.CTkFont("TkDefaultFont", 17, "bold"),border_color="Midnight Blue", border_width=2, hover_color="purple3")

    update.place(x=800, y=700)
    register.place(x=570, y=700)

#register
def getval1():
    global error, back_btn, name_val, dob_val, gender_val, email_val,p_id,phone_val,option1,option2
    name_val = name.get()
    email_val = email.get()
    dob_val = dob.get()
    gender_val = option1.get()
    type_of_patient_val = option2.get()
    phone_val = phone.get()
    k = randint(999,9999)
    p_id.configure(text = "Patient Id : {}".format(k))
    
    if (name_val.strip() not in ("", "Enter name") and dob_val.strip() not in ("", "Enter age") and gender_val != "[Select]" and condition.get().strip()!="Enter past condition" and email_val.strip() not in ("", "Enter email")):
        if type_of_patient_val == "Out Patient":
            db.insert_outpatient(name_val, gender_val, dob_val, phone_val,now,email_val,k)
            print("Outpatient registered")
            success_label = ct.CTkLabel(main_frame, text="Registration confirmed!", text_color="green", font=("TkDefaultFont", 25, "bold"), bg_color="snow2")
            success_label.place(x=680, y=770)
            
        elif type_of_patient_val == "In Patient" and condition.get().strip()!="":
            medcond = condition.get()
            if medcond.split() not in("","Enter condition"):
                db.insert_inpatient(k,name_val,gender_val,dob_val,phone_val,now,None,email_val,medcond)
                print("Inpatient registered")
                success_label = ct.CTkLabel(main_frame, text="Registration confirmed!", text_color="green", font=("TkDefaultFont", 25, "bold"), bg_color="snow2")
                success_label.place(x=680, y=770)
        
    else:
        for widget in main_frame.winfo_children():
            if widget != main_frame.lb:
                widget.place_forget()

        error = ct.CTkLabel(main_frame, text="Please fill all fields", text_color="Black", font=("Times New Roman", 80), bg_color="snow2")
        error.place(x=450, y=300)

        back_btn = ct.CTkButton(main_frame, text="Back", command=restore_ui, text_color="Black", corner_radius=30, height=60,fg_color=("purple", "White"), font=ct.CTkFont("TkDefaultFont", 17, "bold"),border_color="Midnight Blue", border_width=2, hover_color="purple3")
        back_btn.place(relx=0.45, rely=0.9)

#update
def getval2():
    global error, back_btn, name_val, dob_val, gender_val, email_val,p_id,phone_val,type_of_patient_val,p_id
    name_val = name.get()
    email_val = email.get()
    dob_val = dob.get()
    gender_val = option1.get()
    phone_val = phone.get()
    type_of_patient_val = option2.get()

    if (name_val.strip() not in ("", "Enter name") and dob_val.strip() not in ("", "Enter age") and gender_val != "[Select]" and condition.get().strip()!="Enter past condition" and email_val.strip() not in ("", "Enter email") and p_id!=None):
        if type_of_patient_val == "Out Patient":
            
            pat_id = db.get_outpatient_id(email_val)
            p_id.configure(text = "Patient ID : {}".format(pat_id))
            db.update_outpatient(name_val, gender_val, dob_val, phone_val,now, None,email_val,None,pat_id)
            print("Outpatient updated")
            success_label = ct.CTkLabel(main_frame, text="Updation processed!", text_color="green", font=("TkDefaultFont", 25, "bold"), bg_color="snow2")
            success_label.place(x=680, y=770)
            
        elif type_of_patient_val == "In Patient"  and condition.get().strip()!="":
            
            pat_id = db.get_inpatient_id(email_val)
            p_id.configure(text = "Patient ID : {}".format(pat_id))
            information = [name_val,gender_val,dob_val,phone_val,None,now,None,email_val,condition.get()]
            db.update_inpatient(*information,pat_id)
            print("Inpatient updated")
            success_label = ct.CTkLabel(main_frame, text="Updation processed!", text_color="green", font=("TkDefaultFont", 25, "bold"), bg_color="snow2")
            success_label.place(x=680, y=770)
        
    
        
    else:
        for widget in main_frame.winfo_children():
            if widget != main_frame.lb:
                widget.place_forget()

        error = ct.CTkLabel(main_frame, text="Please fill all fields", text_color="Black", font=("Times New Roman", 80), bg_color="snow2")
        error.place(x=450, y=300)

        back_btn = ct.CTkButton(main_frame, text="Back", command=restore_ui, text_color="Black", corner_radius=30, height=60,fg_color=("purple", "White"), font=ct.CTkFont("TkDefaultFont", 17, "bold"),border_color="Midnight Blue", border_width=2, hover_color="purple3")
        back_btn.place(relx=0.45, rely=0.9)

# buttons
register = ct.CTkButton(main_frame, text="Register", command=getval1, width=200, text_color="Black", corner_radius=50,height=60, fg_color=("purple", "White"), font=ct.CTkFont("TkDefaultFont", 17, "bold"),border_color="Midnight Blue", border_width=2, hover_color="purple3")
update = ct.CTkButton(main_frame, text="Update", command=getval2, width=200, text_color="Black", corner_radius=50,height=60, fg_color=("purple", "White"), font=ct.CTkFont("TkDefaultFont", 17, "bold"),border_color="Midnight Blue", border_width=2, hover_color="purple3")

register.place(x=570, y=700)
update.place(x=800, y=700)

#to enable/disable condition widget
def on_patient_type_change(choice):
    if choice == "In Patient":
        condition.configure(state="normal")
    else:
        condition.delete(0, END)
        condition.configure(state="disabled")
        

type_of_patient.configure(command=on_patient_type_change)

root.mainloop()
