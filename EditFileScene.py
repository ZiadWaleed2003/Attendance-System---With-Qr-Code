from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage ,ttk , filedialog , messagebox
import tkinter as tk
from SystemCode import MainSystem
from frame_utils import switch_frame
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame6")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

ms = MainSystem()

def select_File():
    file_path2 = filedialog.askopenfilename()
    ms.set_Df2_For_Edit(file_path2)
    print(file_path2)



def choose_Img():

    global file_path
    file_path = filedialog.askopenfilename()
    print(file_path)


def decode_Img():


    try:
        global data
        img = ms.convert_Path_to_Image(file_path)
        data = ms.Decode_Img(img)

        if data is not None:
            result_var2.set(f"""Decoded QR Code data:\n 
Name : {data["Name"]}
Code : {data["Code"]}
Number : {data["Number"]}
Course : {data["Course"]}
                                    """)
        else:
            result_var2.set(F"No QR code detected, please try again!")
    
    except:

        messagebox.showerror("Error" , "Error While Decoding Please Try Again!")


def add_To_File():
    
     if  data is not None :
            
        try:
            ms.add_Data_To_DataFrame(data)
            print(ms.df)

        except:
            messagebox.showerror("Error", message="Error ! Please try again" )

     else:
        messagebox.showerror("Error", message="Error ! please make sure it's a valid QR Code")



def edit_File_Scene(main_frame , back_frame , save_frame):

    global result_var2
    main_frame.tkraise()
    result_var2 = tk.StringVar()

    canvas = Canvas(
        main_frame,
        bg = "#0E0E0E",
        height = 620,
        width = 920,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        main_frame,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame(save_frame),
        relief="flat"
    )
    button_1.place(
        x=746.0,
        y=545.0,
        width=138.0,
        height=38.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        main_frame,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=select_File,
        relief="flat"
    )
    button_2.place(
        x=352.0,
        y=42.0,
        width=214.0939483642578,
        height=54.98851013183594
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        main_frame,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command= lambda: switch_frame(back_frame),
        relief="flat"
    )
    button_3.place(
        x=31.0,
        y=541.0,
        width=154.0,
        height=45.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        main_frame,
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command= choose_Img,
        relief="flat"
    )
    button_4.place(
        x=321.0,
        y=120.0,
        width=282.0,
        height=45.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        main_frame,
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command= decode_Img,
        relief="flat"
    )
    button_5.place(
        x=370.0,
        y=201.0,
        width=179.0,
        height=46.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        main_frame,
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command= add_To_File,
        relief="flat"
    )
    button_6.place(
        x=310.0,
        y=456.0,
        width=299.0,
        height=63.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        main_frame,
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command= add_To_File,
        relief="flat"
    )
    button_7.place(
        x=305.0,
        y=451.0,
        width=309.0,
        height=73.0
    )

    result_label = ttk.Label(main_frame, textvariable = result_var2)
    result_label.pack(pady=10)
    result_label.place(
            x=352,
            y=335,
            height=50,
            width=220
    )
   
    main_frame.image_refs = [button_image_1, button_image_2, button_image_3, button_image_4, button_image_5, button_image_6,button_image_7]