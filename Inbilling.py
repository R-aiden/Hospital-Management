from tkinter import *
import customtkinter as ct
from PIL import Image,ImageTk,ImageGrab,ImageOps
from database import Connect
from datetime import datetime,timedelta,date
import os

db = Connect()

root = ct.CTk(fg_color="snow2")
root.iconbitmap("C:/Users\chava\Desktop\csc project resources/Logo2.ico")
root.title("Inbilling")
root.geometry("1000x1000")
root.grid_rowconfigure(0,weight = 1)
root.grid_columnconfigure(0,weight = 1)

head = ct.CTkLabel(root, text = "Billing",text_color = "Black",font=("Times New Roman",80),bg_color="snow2")
head.grid(row = 0, column = 0,columnspan = 2, sticky = "n",padx = 200, pady = 50)

id_list1 = db.inpatient_ids()
in_id_list = [str(i[0]) for i in id_list1]
pick = ct.StringVar(value="[Select ID]")
vals = ["[Select ID]"] + in_id_list
        
option = ct.CTkComboBox(master=root, values=vals,variable=pick, text_color="black", fg_color="medium purple2", width=200, height=40, font=("Inter", 20), dropdown_hover_color="grey", button_color="snow2", button_hover_color="grey70", corner_radius=8)
option.set("[Select ID]")
option.place(x=670, y=400)

#background
img = Image.open("C:/Users/chava/Desktop/test.png")
bk = ct.CTkImage(dark_image=img,size = (1700,1700))
lb = ct.CTkLabel(root,image=bk,text="")
lb.place(relx=0, rely=0, relwidth=1, relheight=1)
lb.lower()

def display():
    global pick,price,main_frame,patient_id
    main_frame = ct.CTkFrame(root, fg_color="transparent", width=2000, height=800)
    data = db.get_inpatient(pick.get())
    patient_id,inname,date_of_admission,cond = data
    days_passed = db.get_inpatient_days(pick.get())
    room_type = db.get_room_type(pick.get())
    
    
    date_of_discharge = datetime.strptime(date_of_admission, "%Y-%m-%d").date()+(timedelta(days = days_passed))
    if not days_passed or not room_type:
        
        error = ct.CTkLabel(main_frame,text = "Please choose/enter a valid id",text_color = "Red",font=("Times New Roman",40),bg_color="snow2")
        error.place(x = 670, y = 600)
    if room_type == "Single Room - RS4500":
        price = 4500*int(days_passed)
    elif room_type == "Twin Sharing - RS2500":
        price = 2500*int(days_passed)
    elif room_type == "Triple Sharing - RS2000":
        price = 2000*int(days_passed)
        
    #heading
    head = ct.CTkLabel(main_frame, text = "Billing",text_color = "Black",font=("Times New Roman",80),bg_color="snow2")
    head.place(x = 640, y = 50)
    
    #information
    p_id = ct.CTkLabel(main_frame,text = "Patient ID : {}".format(patient_id),text_color = "Black",font=("Times New Roman",40),bg_color="snow2")
    p_name = ct.CTkLabel(main_frame,text = "Patient Name : {}".format(inname),text_color = "Black",font=("Times New Roman",40),bg_color="snow2")
    dod = ct.CTkLabel(main_frame,text = "Date of discharge : {}".format(date_of_discharge),text_color = "Black",font=("Times New Roman",40),bg_color="snow2")
    doa = ct.CTkLabel(main_frame,text = "Date of admission : {}".format(date_of_admission),text_color = "Black",font=("Times New Roman",40),bg_color="snow2")
    condition =  ct.CTkLabel(main_frame,text = "Condition : {}".format(cond),text_color = "Black",font=("Times New Roman",40),bg_color="snow2")
    cost = ct.CTkLabel(main_frame,text = "Total Cost : {}".format(price),text_color = "Black",font=("Times New Roman",40),bg_color="snow2")

    #placement
    p_id.place(x=250, y=200)
    p_name.place(x=250, y=350)
    cost.place(x=250, y=500)
    condition.place(x = 1000, y = 200)
    dod.place(x=1000, y=500)
    doa.place(x=1000, y=350)

    confirm = ct.CTkButton(main_frame,text = "Print",command = output,width = 200,text_color = "Black",corner_radius = 50,height = 60,fg_color = ("purple","White"),font=ct.CTkFont("TkDefaultFont",17,"bold"),border_color = "Midnight Blue",border_width = 2,hover_color = "purple3")
    confirm.place(x = 650, y = 650)
    
    main_frame.place(x=0, y=0)
    
def output():
    global main_frame, patient_id

    # Get bounding box of the billing frame
    x = root.winfo_rootx() + main_frame.winfo_x()
    y = root.winfo_rooty() + main_frame.winfo_y()
    x1 = x + main_frame.winfo_width()
    y1 = y + main_frame.winfo_height()

    # Force redraw before capture
    root.update()
    img = ImageGrab.grab(bbox=(x, y, x1, y1))

    # Convert to grayscale and autocrop non-empty region
    gray = ImageOps.grayscale(img)
    bbox = gray.getbbox()  # area other than black

    if bbox:
        img = img.crop(bbox)

    # location to save
    save_dir = r"C:\Users\chava\Desktop\Hospital Management\InBills"

    # Save with readable timestamp
    filename = os.path.join(
        save_dir,
        f"Billing_{patient_id}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
    )
    img.save(filename)
    print(f"✅ Billing screenshot saved as {filename}")
    success_label = ct.CTkLabel(main_frame, text="Details printed!", text_color="green", font=("TkDefaultFont", 25, "bold"), bg_color="snow2")
    success_label.place(x=650, y=770)
    
    
select = ct.CTkButton(root,text = "Select",command = display,width = 200,text_color = "Black",corner_radius = 50,height = 60,fg_color = ("purple","White"),font=ct.CTkFont("TkDefaultFont",17,"bold"),border_color = "Midnight Blue",border_width = 2,hover_color = "purple3")
select.place(x = 650, y = 650)

root.mainloop()