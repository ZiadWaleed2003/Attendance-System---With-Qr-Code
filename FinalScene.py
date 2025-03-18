from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame4")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def final_Scene(main_frame):

    main_frame.tkraise()
    

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
    canvas.create_rectangle(
        0.0,
        0.0,
        305.0,
        620.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_text(
        398.0,
        468.0,
        anchor="nw",
        text="All done ! You can close this App now ",
        fill="#FFFFFF",
        font=("Inter SemiBold", 24 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        156.0,
        288.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        599.0,
        160.0,
        image=image_image_2
    )
    
    main_frame.image_refs = [image_image_1, image_image_2 , image_1 , image_2]