from tkinter import *
import customtkinter as ct
from PIL import Image,ImageTk
import subprocess

#main window
root = ct.CTk(fg_color="snow2")
root.iconbitmap("C:/Users\chava\Desktop\csc project resources/Logo2.ico")
root.title("Patient Booking Options")
root.geometry("1000x1000")
root.grid_rowconfigure(0,weight = 1)
root.grid_columnconfigure(0,weight = 1)

#background
img = Image.open("C:/Users/chava/Desktop/test.png")
bk = ct.CTkImage(dark_image=img,size = (1700,1700))
lb = ct.CTkLabel(root,image=bk,text="")
lb.place(relx=0, rely=0, relwidth=1, relheight=1)
lb.lower()


main_head = ct.CTkLabel(root, text = "Select action",text_color = "Black",font=("Times New Roman",80),bg_color="snow2")
main_head.grid(row = 0, column = 0,columnspan = 2, sticky = "n",padx = 200, pady = 50)
image1 = Image.open("C:/Users/chava/Desktop/csc project resources/OutPatient.jpeg")
image2 = Image.open("C:/Users/chava/Desktop/csc project resources/InPatient.png")
img1 = ct.CTkImage(dark_image = image1,size = (300,300))
img2 = ct.CTkImage(dark_image = image2,size = (300,300))

#opening respective windows
def Out():
    subprocess.Popen(["python","C:/Users/chava/Desktop/Hospital Management/OutBooking.py"])
def In():
    subprocess.Popen(["python","C:/Users/chava/Desktop/Hospital Management/InBooking.py"])
    
#options
update_label = ct.CTkLabel(root,text = "Admitted Patient",text_color = "Black",font = ("Helvetica",30,"bold"),bg_color = "snow2")
register_label = ct.CTkLabel(root,text = "Visiting Patient",text_color = "Black",font = ("Helvetica",30,"bold"),bg_color = "snow2")
update = ct.CTkButton(root, text = "",image = img2,width = 100,corner_radius = 50,height = 60,fg_color = ("purple","White"),border_color = "Midnight Blue",border_width = 2,hover_color = "snow2",command = In)
new = ct.CTkButton(root, text = "",image = img1,width = 100,corner_radius = 50,height = 60,command = Out,fg_color = ("purple","White"),border_color = "Midnight Blue",border_width = 2,hover_color = "snow2")

#placement
update.place(x = 300, y = 250)
new.place(x = 900, y = 250)
update_label.place(x = 340, y = 580)
update_label.lift()
register_label.place(x = 960, y = 580)
register_label.lift()

root.mainloop()
