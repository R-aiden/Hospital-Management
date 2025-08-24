from tkinter import *
import customtkinter as ct
from PIL import Image,ImageTk,ImageGrab,ImageOps
from database import Connect
from datetime import datetime
import os

db = Connect()

root = ct.CTk(fg_color="snow2")
root.iconbitmap("C:/Users\chava\Desktop\csc project resources/Logo2.ico")
root.title("OutBilling")
root.geometry("1000x1000")
root.grid_rowconfigure(0,weight = 1)
root.grid_columnconfigure(0,weight = 1)

head = ct.CTkLabel(root, text = "Billing",text_color = "Black",font=("Times New Roman",80),bg_color="snow2")
head.grid(row = 0, column = 0,columnspan = 2, sticky = "n",padx = 200, pady = 50)


out_list = db.get_outpatient_ids()
out_id_list = [str(i) for i in out_list]
pick = ct.StringVar(value="[Select]")
vals = ["[Select"] + out_id_list
        
option = ct.CTkComboBox(master=root, values=vals,variable=pick, text_color="black", fg_color="medium purple2", width=200, height=40, font=("Inter", 20), dropdown_hover_color="grey", button_color="snow2", button_hover_color="grey70", corner_radius=8)
option.set("[Select]")
option.place(x=670, y=400)


#background
img = Image.open("C:/Users/chava/Desktop/test.png")
bk = ct.CTkImage(dark_image=img,size = (1700,1700))
lb = ct.CTkLabel(root,image=bk,text="")
lb.place(relx=0, rely=0, relwidth=1, relheight=1)
lb.lower()

def display():
    global main_frame,patient_id
    main_frame = ct.CTkFrame(root, fg_color="snow2", width=2000, height=800)
    patient_name,cond,patient_id = db.get_outpatient(pick.get())
    
    #heading
    head = ct.CTkLabel(main_frame, text = "Billing",text_color = "Black",font=("Times New Roman",80),bg_color="snow2")
    head.place(x = 640, y = 50)
    
    #information
    p_id = ct.CTkLabel(main_frame,text = "Patient Id : {}".format(patient_id),text_color = "Black",font=("Times New Roman",40),bg_color="snow2")
    p_name = ct.CTkLabel(main_frame,text = "Patient Name : {}".format(patient_name),text_color = "Black",font=("Times New Roman",40),bg_color="snow2")
    condition = ct.CTkLabel(main_frame,text = "Condition : {}".format(cond),text_color = "Black",font=("Times New Roman",40),bg_color="snow2")
    cost = ct.CTkLabel(main_frame,text = "Total Cost : 500",text_color = "Black",font=("Times New Roman",40),bg_color="snow2")

    #placement
    p_id.place(x=250, y=200)
    p_name.place(x=250, y=500)
    cost.place(x=1000, y=500)
    condition.place(x=1000, y=200)
    
    confirm = ct.CTkButton(main_frame,text = "Print",width = 200,command = output,text_color = "Black",corner_radius = 50,height = 60,fg_color = ("purple","White"),font=ct.CTkFont("TkDefaultFont",17,"bold"),border_color = "Midnight Blue",border_width = 2,hover_color = "purple3")
    confirm.place(x = 650, y = 650)
    
    main_frame.place(x=0, y=0)
    
    root.update()  # ensure all widgets are drawn
    
"""to extract the image"""
from datetime import datetime
from PIL import ImageGrab

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
    bbox = gray.getbbox()  # bounding box of non-black area

    if bbox:
        img = img.crop(bbox)

    # Ensure folder exists
    save_dir = r"C:\Users\chava\Desktop\Hospital Management\OutBills"

    # Save with readable timestamp
    filename = os.path.join(
        save_dir,
        f"Billing_{patient_id}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
    )
    img.save(filename)
    print(f"✅ Billing screenshot saved as {filename}")
    success_label = ct.CTkLabel(main_frame, text="Details printed!", text_color="green", font=("TkDefaultFont", 25, "bold"), bg_color="snow2")
    success_label.place(x=650, y=770)



select = ct.CTkButton(root,text = "Select",width = 200,command = display,text_color = "Black",corner_radius = 50,height = 60,fg_color = ("purple","White"),font=ct.CTkFont("TkDefaultFont",17,"bold"),border_color = "Midnight Blue",border_width = 2,hover_color = "purple3")
select.place(x = 650, y = 650)

root.mainloop()
