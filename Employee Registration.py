from tkinter import *
import customtkinter as ct
from PIL import Image, ImageTk
from database import Connect
from random import randint

db = Connect()

root = ct.CTk(fg_color="snow2")
main_frame = ct.CTkFrame(root, fg_color="snow2")
root.iconbitmap("C:/Users/chava/Desktop/csc project resources/Logo2.ico")
root.title("Employee Registration")
root.geometry("1000x1000")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

# variables
option1 = ct.StringVar(value="[Select]")
option2 = ct.StringVar(value="[Select]")
error = None
back_btn = None

# entry widgets
name = ct.CTkEntry(main_frame, width=300, placeholder_text="Enter name", placeholder_text_color="Grey30", corner_radius=30, height=50, text_color="Black", fg_color=("purple3", "snow2"), justify="center", font=("TkDefaultFont", 20, "bold"), border_color="Midnight Blue", border_width=2)
phone = ct.CTkEntry(main_frame, width=300, placeholder_text="Enter phone number", placeholder_text_color="Grey30", corner_radius=30,height=50, text_color="Black", fg_color=("purple3", "snow2"), justify="center", font=("TkDefaultFont", 20, "bold"),border_color="Midnight Blue", border_width=2)
email = ct.CTkEntry(main_frame, width=300, corner_radius=30, placeholder_text="Enter email", placeholder_text_color="Grey30",height=50, text_color="Black", fg_color=("purple3", "snow2"), justify="center", font=("TkDefaultFont", 20, "bold"),border_color="Midnight Blue", border_width=2)
dob = ct.CTkEntry(main_frame, width=300, corner_radius=30, placeholder_text="Enter dob", placeholder_text_color="Grey30",height=50, text_color="Black", fg_color=("purple3", "snow2"), justify="center", font=("TkDefaultFont", 20, "bold"),border_color="Midnight Blue", border_width=2)

#labels
gender_label = ct.CTkLabel(main_frame, text="Gender : ", text_color="Black", font=("TkinterDefaultFont", 30), bg_color="snow2")
e_code = ct.CTkLabel(main_frame, text="Employee Id : ", text_color="Black", font=("TkinterDefaultFont", 30), bg_color="snow2")
depar = ct.CTkLabel(main_frame, text="Select department : ", text_color="Black", font=("TkinterDefaultFont", 30), bg_color="snow2")

#OPTIONMENUS
dept = ct.CTkOptionMenu(main_frame, values=["[Select]", "Doctor", "Admin","Nurse"], variable=option2, text_color="Black",fg_color="medium purple2", width=150, height=40, font=("Inter", 20), dropdown_hover_color="Grey",button_color="snow2", button_hover_color="grey70")
gender = ct.CTkOptionMenu(main_frame, values=["[Select]", "Male", "Female"], variable=option1, text_color="Black",fg_color="medium purple2", width=150, height=40, font=("Inter", 20), dropdown_hover_color="Grey",button_color="snow2", button_hover_color="grey70")


#login
user = ct.CTkEntry(main_frame, width=300, placeholder_text="Create username", placeholder_text_color="Grey30", corner_radius=30,height=50, text_color="Black", fg_color=("purple3", "snow2"), justify="center", font=("TkDefaultFont", 20, "bold"),border_color="Midnight Blue", border_width=2)
password = ct.CTkEntry(main_frame, width=300, placeholder_text="Create password", placeholder_text_color="Grey30", corner_radius=30,height=50, text_color="Black", fg_color=("purple3", "snow2"), justify="center", font=("TkDefaultFont", 20, "bold"),border_color="Midnight Blue", border_width=2)
user.place(x = 170, y = 600)
password.place(x = 1100,y = 600)

# placing entry widgets
name.place(x=170, y=300)
dob.place(x=1100, y=300)
gender_label.place(x=170, y=450)
gender.place(x=350, y=450)
phone.place(x=600, y=450)
email.place(x=1100, y=450)
e_code.place(x = 600, y = 310)
dept.place(x = 900, y = 610)
depar.place(x = 600, y = 610)

# header
head = ct.CTkLabel(main_frame, text="Employee Registration", text_color="Black", font=("Times New Roman", 80), bg_color="snow2")
head.place(x=425, y=50)

def restore_ui():
    global error, back_btn, name, phone, dob, gender, email, option1,option2

    # Remove error and back button
    if back_btn:
        back_btn.destroy()
        back_btn = None
    if error:
        error.destroy()
        error = None
        
    head = ct.CTkLabel(main_frame, text="Employee Registration", text_color="Black",font=("Times New Roman", 80), bg_color="snow2")               
    head.place(x=425, y=50)

    # Reset dropdown option
    option1.set("[Select]")
    option2.set("[Select]")

    # Destroy existing input widgets
    for widget in [name, phone, dob, email, gender]:
        if widget:
            widget.destroy()

    # entry widgets
    name = ct.CTkEntry(main_frame, width=300, placeholder_text="Enter name", placeholder_text_color="Grey30", corner_radius=30, height=50, text_color="Black", fg_color=("purple3", "snow2"), justify="center", font=("TkDefaultFont", 20, "bold"), border_color="Midnight Blue", border_width=2)
    phone = ct.CTkEntry(main_frame, width=300, placeholder_text="Enter phone number", placeholder_text_color="Grey30", corner_radius=30,height=50, text_color="Black", fg_color=("purple3", "snow2"), justify="center", font=("TkDefaultFont", 20, "bold"),border_color="Midnight Blue", border_width=2)
    email = ct.CTkEntry(main_frame, width=300, corner_radius=30, placeholder_text="Enter email", placeholder_text_color="Grey30",height=50, text_color="Black", fg_color=("purple3", "snow2"), justify="center", font=("TkDefaultFont", 20, "bold"),border_color="Midnight Blue", border_width=2)
    dob = ct.CTkEntry(main_frame, width=300, corner_radius=30, placeholder_text="Enter dob", placeholder_text_color="Grey30",height=50, text_color="Black", fg_color=("purple3", "snow2"), justify="center", font=("TkDefaultFont", 20, "bold"),border_color="Midnight Blue", border_width=2)

    #labels
    gender_label = ct.CTkLabel(main_frame, text="Gender : ", text_color="Black", font=("TkinterDefaultFont", 30), bg_color="snow2")
    e_code = ct.CTkLabel(main_frame, text="Employee Id : ", text_color="Black", font=("TkinterDefaultFont", 30), bg_color="snow2")
    depar = ct.CTkLabel(main_frame, text="Select department : ", text_color="Black", font=("TkinterDefaultFont", 30), bg_color="snow2")
    
    #OPTIONMENUS
    dept = ct.CTkOptionMenu(main_frame, values=["[Select]", "Doctor", "Admin","Nurse"], variable=option2, text_color="Black",fg_color="medium purple2", width=150, height=40, font=("Inter", 20), dropdown_hover_color="Grey",button_color="snow2", button_hover_color="grey70")
    gender = ct.CTkOptionMenu(main_frame, values=["[Select]", "Male", "Female"], variable=option1, text_color="Black",fg_color="medium purple2", width=150, height=40, font=("Inter", 20), dropdown_hover_color="Grey",button_color="snow2", button_hover_color="grey70")


    #login
    user = ct.CTkEntry(main_frame, width=300, placeholder_text="Create username", placeholder_text_color="Grey30", corner_radius=30,height=50, text_color="Black", fg_color=("purple3", "snow2"), justify="center", font=("TkDefaultFont", 20, "bold"),border_color="Midnight Blue", border_width=2)
    password = ct.CTkEntry(main_frame, width=300, placeholder_text="Create password", placeholder_text_color="Grey30", corner_radius=30,height=50, text_color="Black", fg_color=("purple3", "snow2"), justify="center", font=("TkDefaultFont", 20, "bold"),border_color="Midnight Blue", border_width=2)
    user.place(x = 170, y = 600)
    password.place(x = 1100,y = 600)

    # placing entry widgets
    name.place(x=170, y=300)
    dob.place(x=1100, y=300)
    gender_label.place(x=200, y=450)
    gender.place(x=350, y=450)
    phone.place(x=650, y=450)
    email.place(x=1100, y=450)
    e_code.place(x = 600, y = 310)
    dept.place(x = 800, y = 610)
    depar.place(x = 520, y = 610)

    # Buttons
    register = ct.CTkButton(main_frame, text="Register", command=getval1, width=200,text_color="Black", corner_radius=50, height=60,fg_color=("purple", "White"),font=ct.CTkFont("TkDefaultFont", 17, "bold"),border_color="Midnight Blue", border_width=2, hover_color="purple3")
    update = ct.CTkButton(main_frame, text="Update", command=getval2, width=200,text_color="Black", corner_radius=50, height=60,fg_color=("purple", "White"),font=ct.CTkFont("TkDefaultFont", 17, "bold"),border_color="Midnight Blue", border_width=2, hover_color="purple3")

    update.place(x=800, y=700)
    register.place(x=570, y=700)

#register
def getval1():
    global error, back_btn, name_val, phone_val, dob_val, gender_val, email_val,user_id,pass_id,dept,i
    name_val = name.get()
    phone_val = phone.get()
    email_val = email.get()
    dob_val = dob.get()
    gender_val = option1.get()
    user_id = user.get()
    pass_id = password.get()
    dept_val = option2.get()
    i = randint(99999,999999)

    if (name_val.strip() not in ("", "Enter name") and dob_val.strip() not in ("", "Enter dob") and gender_val != "[Select]" and phone_val.strip() not in ("", "Enter phone number") and email_val.strip() not in ("", "Enter email") and user_id not in ("", "Create username") and pass_id not in ("", "Create password") and dept_val!="[Select]"):
        if not db.check_info(user_id):
            if dept_val == "Admin":
                
                information = [i,name_val,25000,dob_val,phone_val,gender_val,email_val,user_id,pass_id]
                db.insert_admin(*information)
                e_code.configure(text = "Employee Id : {}".format(i))
                success_label = ct.CTkLabel(main_frame, text="Admin Registration confirmed!", text_color="green", font=("TkDefaultFont", 25, "bold"), bg_color="snow2")
                success_label.place(x=680, y=770)
                
            elif dept_val == "Doctor":
                
                information = [i,name_val,100000,dob_val,phone_val,email_val,gender_val,user_id,pass_id]
                db.insert_doctor(*information)
                e_code.configure(text = "Employee Id : {}".format(i))
                
                for widget in main_frame.winfo_children():
                    widget.place_forget()
                        
                select_field = ct.CTkLabel(main_frame, text="Select field : ", text_color="Black", font=("TkinterDefaultFont", 50), bg_color="snow2")
                select_field.place(x = 500, y = 500)
                
                optionnew = ct.StringVar(value="[Select]")
                fields = ct.CTkOptionMenu(main_frame, values=["[Select]", "Dermatologist", "Cardiologist","Opthalmologist","Dentist"], variable=optionnew, text_color="Black",fg_color="medium purple2", width=150, height=40, font=("Inter", 20), dropdown_hover_color="Grey",button_color="snow2", button_hover_color="grey70")
                fields.place(x = 800, y = 520)
                
                def insert(field,cd):
                    db.insert_field_doctor(field,cd)
                    #print("Successfully inserted",field)
                    success_label = ct.CTkLabel(main_frame, text="Doctor Registration confirmed!", text_color="green", font=("TkDefaultFont", 25, "bold"), bg_color="snow2")
                    success_label.place(x=680, y=770)
                
                choose = ct.CTkButton(main_frame, text="Choose", command=lambda:insert(optionnew.get(),i), text_color="Black", corner_radius=30, height=60,fg_color=("purple", "White"), font=ct.CTkFont("TkDefaultFont", 17, "bold"),border_color="Midnight Blue", border_width=2, hover_color="purple3")
                choose.place(x=800, y=700)
                
            elif dept_val == "Nurse":
                
                db.insert_nurse(i,name_val,25000,dob_val,phone_val,user_id,pass_id,email_val,gender_val)
                e_code.configure(text = "Employee Id : {}".format(i))
                success_label = ct.CTkLabel(main_frame, text="Nurse Registration confirmed!", text_color="green", font=("TkDefaultFont", 25, "bold"), bg_color="snow2")
                success_label.place(x=680, y=770)
                
        else:
            # Show duplicate email warning
            duplicate_label = ct.CTkLabel(main_frame, text="Username already exists!", text_color="red", font=("TkDefaultFont", 25, "bold"), bg_color="snow2")
            duplicate_label.place(x=680, y=770)
    else:
        for widget in main_frame.winfo_children():
            widget.place_forget()

        error = ct.CTkLabel(main_frame, text="Please fill all fields", text_color="Black", font=("Times New Roman", 80), bg_color="snow2")
        error.place(x=450, y=300)

        back_btn = ct.CTkButton(main_frame, text="Back", command=restore_ui, text_color="Black", corner_radius=30, height=60,fg_color=("purple", "White"), font=ct.CTkFont("TkDefaultFont", 17, "bold"),border_color="Midnight Blue", border_width=2, hover_color="purple3")
        back_btn.place(relx=0.45, rely=0.9)

#update
def getval2():
    global error, back_btn, name_val, phone_val, dob_val, gender_val, email_val,user_id,pass_id,dept
    name_val = name.get()
    phone_val = phone.get()
    email_val = email.get()
    dob_val = dob.get()
    gender_val = option1.get()
    dept_val = option2.get()
    user_id = user.get()
    pass_id = password.get()
    
    if (name_val.strip() not in ("", "Enter name") and dob_val.strip() not in ("", "Enter dob") and gender_val != "[Select]" and phone_val.strip() not in ("", "Enter phone number") and email_val.strip() not in ("", "Enter email") and user_id not in ("", "Create username") and pass_id not in ("", "Create password") and dept_val !="[Select]"):
        if dept_val == "Admin":
            
            e_id = db.get_id_admin(email_val)
            if not e_id:
                er_label = ct.CTkLabel(main_frame, text="No such record found!", text_color="red", font=("TkDefaultFont", 25, "bold"), bg_color="snow2")
                er_label.place(x=680, y=770)
                return
            
            information = [e_id,name_val,dob_val,phone_val,gender_val, email_val,user_id,pass_id]
            db.update_admin(*information)
            e_code.configure(text = "Employee Id : {}".format(db.get_id_admin(email_val)))
            success_label = ct.CTkLabel(main_frame, text="Admin Updation confirmed!", text_color="green", font=("TkDefaultFont", 25, "bold"), bg_color="snow2")
            success_label.place(x=680, y=770)
            
        elif dept_val == "Doctor":
            
            e_id = db.get_id_doctor(email_val)
            if not e_id:
                er_label = ct.CTkLabel(main_frame, text="No such record found!", text_color="red", font=("TkDefaultFont", 25, "bold"), bg_color="snow2")
                er_label.place(x=680, y=770)
                return
            
            information = [e_id,name_val,dob_val,phone_val,email_val,gender_val,user_id,pass_id]
            db.update_doctor(*information)
            e_code.configure(text = "Employee Id : {}".format(db.get_id_doctor(email_val)))
            success_label = ct.CTkLabel(main_frame, text="Doctor Updation confirmed!", text_color="green", font=("TkDefaultFont", 25, "bold"), bg_color="snow2")
            success_label.place(x=680, y=770)
            
        elif dept_val == "Nurse":
            
            e_id = db.get_id_nurse(email_val)
            if not e_id:
                er_label = ct.CTkLabel(main_frame, text="No such record found!", text_color="red", font=("TkDefaultFont", 25, "bold"), bg_color="snow2")
                er_label.place(x=680, y=770)
                return
            
            information = [e_id,name_val,dob_val,phone_val,user_id,pass_id,email_val,gender_val]
            db.update_nurse(*information)
            e_code.configure(text = "Employee Id : {}".format(db.get_id_nurse(email_val)))
            success_label = ct.CTkLabel(main_frame, text="Nurse Updation confirmed!", text_color="green", font=("TkDefaultFont", 25, "bold"), bg_color="snow2")
            success_label.place(x=680, y=770)
        
    else:
        for widget in main_frame.winfo_children():
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

root.mainloop()

