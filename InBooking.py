from tkinter import *
import customtkinter as ct
from PIL import Image,ImageTk
from random import randint
from database import Connect

db = Connect()

#main window
root = ct.CTk(fg_color = "snow2")
main_frame = ct.CTkFrame(root,fg_color = "transparent")
root.iconbitmap(r"C:/Users/chava/Desktop/csc project resources/Logo2.ico")
root.title("In Patient Booking")
root.geometry("1000x1000")
root.grid_rowconfigure(0,weight = 1)
root.grid_columnconfigure(0,weight = 1)
head = ct.CTkLabel(main_frame, text = "Room allocation",text_color = "Black",font=("Times New Roman",80),bg_color="snow2")
head.place(x = 500, y = 50)

main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

#roomid
k = randint(999,9999)
room_id = ct.CTkLabel(main_frame, text = "Room id : {} ".format(k),text_color = "Black",font = ("TkinterDefaultFont",30),bg_color = "snow2")

#department options
dept = ct.CTkLabel(main_frame, text = "Select department :",text_color = "Black",font = ("TkinterDefaultFont",30),bg_color = "snow2")
doctor = ct.CTkLabel(main_frame, text = "Select doctor :",text_color = "Black",font = ("TkinterDefaultFont",30),bg_color = "snow2")
durationlabel = ct.CTkLabel(main_frame, text = "Enter duration(in days) :",text_color = "Black",font = ("TkinterDefaultFont",30),bg_color = "snow2")
type_of_room = ct.CTkLabel(main_frame, text = "Select room type :",text_color = "Black",font = ("TkinterDefaultFont",30),bg_color = "snow2")

#placement
dept.place(x = 300, y = 300)
doctor.place(x = 900, y = 300)
durationlabel.place(x = 900, y = 450)
type_of_room.place(x = 300, y = 445)
room_id.place(x = 650, y = 200)

#retrieval
option1 = ct.StringVar(value="[Select]")
option2 = ct.StringVar(value="[Select]")
option3 = ct.StringVar(value="[Select]")

#list of doctors
t = db.get_doctors()
l = ["-".join(tup) for tup in t ]

#options and extra details
duration = ct.CTkEntry(main_frame,width = 200,placeholder_text = "Enter duration",placeholder_text_color = "Grey30",corner_radius=30,height = 50,text_color = "Black",fg_color = ("purple3","snow2"),justify = "center",font=("TkDefaultFont",20,"bold"),border_color = "Midnight Blue",border_width = 2)
doctor_options = ct.CTkOptionMenu(main_frame, values = l,variable = option2,text_color = "Black",font = ("Inter",20),fg_color = "medium purple2",width = 150, height = 40,dropdown_hover_color = "Grey",button_color = "snow2",button_hover_color = "grey70")
depar = ct.CTkOptionMenu(main_frame, values = ["[Select]","Dermatology","Cardiology","Opthalmology","Dentistry"],variable = option1,text_color = "Black",fg_color = "medium purple2",width = 150, height = 40,font = ("Inter",20),dropdown_hover_color = "Grey",button_color = "snow2",button_hover_color = "grey70")
type_of_room = ct.CTkOptionMenu(main_frame, values = ["[Select]","Single Room - RS4500","Twin Sharing - RS2500","Triple Sharing - RS2000"],variable = option3,text_color = "Black",fg_color = "medium purple2",width = 150, height = 40,font = ("Inter",20),dropdown_hover_color = "Grey",button_color = "snow2",button_hover_color = "grey70")
patient_id = ct.CTkEntry(main_frame, width=300, placeholder_text="Enter Patient ID", placeholder_text_color="Grey30", corner_radius=30,height=50, text_color="Black", fg_color=("purple3", "snow2"), justify="center", font=("TkDefaultFont", 20, "bold"),border_color="Midnight Blue", border_width=2)

#placement
duration.place(x = 1250, y = 445)
depar.place(x = 575, y = 300)
doctor_options.place(x=1100, y = 300)
type_of_room.place(x = 575, y = 445)
patient_id.place(x = 627, y = 600)


#to restore ui
def restore_ui():
    global error,back_btn,department,doctor,type_of_room_val,duration,department,condition,patient_id
    department = doctor = type_of_room_val = duration = name =  ""
    if back_btn:
        back_btn.destroy()
        back_btn = None
    if error:
        error.destroy()
        error = None
    
    head = ct.CTkLabel(main_frame, text = "Book a room",text_color = "Black",font=("TkinterDefaultFont",80),bg_color="snow2")
    head.place(x = 580, y = 50)
    dept = ct.CTkLabel(main_frame, text = "Select department :",text_color = "Black",font = ("TkinterDefaultFont",30),bg_color = "snow2")
    doctor = ct.CTkLabel(main_frame, text = "Select doctor :",text_color = "Black",font = ("TkinterDefaultFont",30),bg_color = "snow2")
    durationlabel = ct.CTkLabel(main_frame, text = "Enter duration(in days):",text_color = "Black",font = ("TkinterDefaultFont",30),bg_color = "snow2")
    type_of_room = ct.CTkLabel(main_frame, text = "Select room type :",text_color = "Black",font = ("TkinterDefaultFont",30),bg_color = "snow2")
    room_id = ct.CTkLabel(main_frame, text = "Room id : {}".format(k),text_color = "Black",font = ("TkinterDefaultFont",30),bg_color = "snow2")
    
    dept.place(x = 300, y = 300)
    doctor.place(x = 900, y = 300)
    durationlabel.place(x = 900, y = 450)
    type_of_room.place(x = 300, y = 445)
    room_id.place(x = 900, y = 600)

    duration = ct.CTkEntry(main_frame,width = 200,placeholder_text = "Enter duration",placeholder_text_color = "Grey30",corner_radius=30,height = 50,text_color = "Black",fg_color = ("purple3","snow2"),justify = "center",font=("TkDefaultFont",20,"bold"),border_color = "Midnight Blue",border_width = 2)
    doctor_options = ct.CTkOptionMenu(main_frame, values = l,variable = option2,text_color = "Black",font = ("Inter",20),fg_color = "medium purple2",width = 150, height = 40,dropdown_hover_color = "Grey",button_color = "snow2",button_hover_color = "grey70")
    depar = ct.CTkOptionMenu(main_frame, values = ["[Select]","Dermatology","Cardiology","Opthalmology","Dentistry"],variable = option1,text_color = "Black",fg_color = "medium purple2",width = 150, height = 40,font = ("Inter",20),dropdown_hover_color = "Grey",button_color = "snow2",button_hover_color = "grey70")
    type_of_room = ct.CTkOptionMenu(main_frame, values = ["[Select]","Single Room - RS4500","Twin Sharing - RS2500","Triple Sharing - RS2000"],variable = option3,text_color = "Black",fg_color = "medium purple2",width = 150, height = 40,font = ("Inter",20),dropdown_hover_color = "Grey",button_color = "snow2",button_hover_color = "grey70")
    patient_id= ct.CTkEntry(main_frame, width=300, placeholder_text="Enter Patient ID", placeholder_text_color="Grey30", corner_radius=30,height=50, text_color="Black", fg_color=("purple3", "snow2"), justify="center", font=("TkDefaultFont", 20, "bold"),border_color="Midnight Blue", border_width=2)
    
    duration.place(x = 1250, y = 445)
    depar.place(x = 575, y = 300)
    doctor_options.place(x=1100, y = 300)
    type_of_room.place(x = 575, y = 445)
    patient_id.place(x = 627, y = 600)
    
    confirm = ct.CTkButton(main_frame,text = "Confirm",width = 200,command = getval,text_color = "Black",corner_radius = 50,height = 60,fg_color = ("purple","White"),font=ct.CTkFont("TkDefaultFont",17,"bold"),border_color = "Midnight Blue",border_width = 2,hover_color = "purple3")
    confirm.place(x = 680, y = 700)
        
def getval():
    global error,back_btn,department,doctor,type_of_room_val,duration_get,department,patient_id_val,room_id
    department = option1.get()
    doctor = option2.get()
    if duration.get():
        duration_get = int(duration.get())
    type_of_room_val = option3.get()
    room_id_val = k
    patient_id_val = patient_id.get()
    
    if department!="[Select]" and doctor!="[Select]" and duration_get!="" and type_of_room_val!="[Select]" and patient_id_val not in("","Enter Patient ID"):
        state = db.insert_room(room_id_val,doctor,type_of_room_val,duration_get,department,patient_id_val)
        if state:
            success_label = ct.CTkLabel(main_frame, text="Booking confirmed!", text_color="green", font=("TkDefaultFont", 25, "bold"), bg_color="snow2")
            success_label.place(x=680, y=770)
        else:
            error2 = ct.CTkLabel(main_frame, text="Please register as a patient first!", text_color="red", font=("TkDefaultFont", 25, "bold"), bg_color="snow2")
            error2.place(x=610, y=770)
    
    else:
        for widget in main_frame.winfo_children():
            widget.destroy()
            room_id.destroy()
                
        error = ct.CTkLabel(main_frame, text = "Please fill all fields",text_color = "Black",font=("Times New Roman",80),bg_color="snow2")
        error.place(x = 450, y = 300)
        back_btn = ct.CTkButton(main_frame, text="Back", command=restore_ui,text_color="Black", corner_radius=30, height=60,fg_color=("purple", "White"), font=ct.CTkFont("TkDefaultFont", 17, "bold"),border_color="Midnight Blue", border_width=2, hover_color="purple3")
        back_btn.place(relx=0.45, rely=0.9)

#buttons and entry field
confirm = ct.CTkButton(main_frame,text = "Confirm",width = 200,command = getval,text_color = "Black",corner_radius = 50,height = 60,fg_color = ("purple","White"),font=ct.CTkFont("TkDefaultFont",17,"bold"),border_color = "Midnight Blue",border_width = 2,hover_color = "purple3")
confirm.place(x = 680, y = 700)

if __name__ == "__main__":
    root.mainloop()