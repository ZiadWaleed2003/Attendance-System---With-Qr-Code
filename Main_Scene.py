from pathlib import Path
from tkinter import Canvas, Button, PhotoImage , Frame
from frame_utils import switch_frame
import tkinter as tk
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def main_Scene(main_frame , camera_frame , file_frame , edit_frame):
   

    main_frame.tkraise()
   
    canvas = Canvas(
        main_frame,
        bg="#0E0E0E",
        height=620,
        width=920,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        0.0,
        0.0,
        307.0,
        620.0,
        fill="#2A2929",
        outline=""
    )

    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(153.0, 357.0, image=image_image_1)
    
    canvas.create_text(
        33.0,
        56.0,
        anchor="nw",
        text="QR Code Scanner",
        fill="#FFFFFF",
        font=("JacquesFrancois Regular", 28 * -1)
    )

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(
        main_frame,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame(file_frame),
        relief="flat"
    )
    button_1.place(
        x=460.0,
        y=300.0,
        width=297.0,
        height=59.0
    )


    button_image_3 = PhotoImage(file=relative_to_assets("EditFile.png"))
    button_3 = Button(
        main_frame,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame(edit_frame),
        relief="flat"
    )
    button_3.place(
        x=490.0,
        y=420.0,
    )

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(
        main_frame,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch_frame(camera_frame),
        relief="flat"
    )
    button_2.place(
        x=460.0,
        y=186.0,
        width=297.0,
        height=59.0
    )

    main_frame.image_refs = [button_image_1, button_image_2, image_1, image_image_1 , button_image_3 ]

    
