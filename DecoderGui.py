import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import cv2
from SystemCode import MainSystem
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from frame_utils import switch_frame


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame5")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class Gui:

    def __init__(self):
        self.vid = None
        self.frame = None
        self.src = 0
        self.system = MainSystem()  # Create an instance of MainSystem
        self.ip = None

    def set_src(self, src):
        self.src = src

    def start_video(self):
        if self.vid is None:
            self.vid = cv2.VideoCapture(self.src)
            if not self.vid.isOpened():
                messagebox.showerror("Error", "Could not open video device")
                return

        cv2.namedWindow("Video Stream", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Video Stream", 640, 460)  # Set your desired window size here
        self.update_frame()

    def update_frame(self):
        if self.vid is None:
            return

        ret, frame = self.vid.read()
        if ret:
            self.frame = frame
            cv2.imshow("Video Stream", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('c'):
                self.capture_and_decode()
            elif key == ord('q'):
                self.vid.release()
                cv2.destroyAllWindows()
                self.vid = None
                return
        self.window.after(10, self.update_frame)

    def capture_and_decode(self):
        if self.frame is not None:
            self.result = self.system.Decode_Img(self.frame)  # Use the MainSystem instance
            
            if self.result is not None:
                self.result_var.set(f"""Decoded QR Code data:\n 
Name : {self.result["Name"]}
Code : {self.result["Code"]}
Number : {self.result["Number"]}
Course : {self.result["Course"]}
                                    """)
            else:
                self.result_var.set("No QR code detected, please try again!")

            # Do not close the window if the QR code is not detected
            cv2.destroyAllWindows()
            self.vid.release()
            self.vid = None

    def on_closing(self):
        if self.vid is not None:
            self.vid.release()
            cv2.destroyAllWindows()
        self.window.destroy()

    def ip_Setter(self):
        self.ip = self.entry_1.get()  # Get the text from the entry widget
        if self.ip is not None:
            if not self.ip.startswith("http"):
                self.ip = 0
                self.set_src(self.ip)
            else:
                self.ip += "/video"
                self.set_src(self.ip)

    def add_Student_controller(self):

        result_var2 = str(self.result_var)
        

        if  result_var2 != "No QR code detected, please try again!" :
            try:
                self.system.add_Data_To_DataFrame(data=self.result)
                print(self.system.df)

            except:
                messagebox.showerror("Error", message="Error ! Please try again" )

        else:
            messagebox.showerror("Error", message="Error ! please make sure it's a valid QR Code")

    def camera_gui(self, window, main_frame, back_frame, save_frame):
        main_frame.tkraise()
        self.window = window
        self.window.geometry("920x620")
        self.window.configure(bg="#0E0E0E")
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.result_var = tk.StringVar()

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
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            main_frame,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.start_video(),
            relief="flat"
        )
        button_1.place(
            x=357.0,
            y=262.0,
            width=201.0,
            height=55.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            main_frame,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command= self.add_Student_controller,
            relief="flat"
        )
        button_2.place(
            x=357.0,
            y=440.0,
            width=201.0,
            height=55.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            main_frame,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: switch_frame(back_frame),
            relief="flat"
        )
        button_3.place(
            x=43.0,
            y=530.0,
            width=190.0,
            height=55.0
        )

        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        button_4 = Button(
            main_frame,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: switch_frame(save_frame),
            relief="flat"
        )
        button_4.place(
            x=703.0,
            y=533.0,
            width=190.0,
            height=55.0
        )

        button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        button_5 = Button(
            main_frame,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.capture_and_decode,
            relief="flat"
        )
        button_5.place(
            x=337.0,
            y=349.0,
            width=240.0,
            height=63.0
        )

        canvas.create_text(
            189.0,
            54.0,
            anchor="nw",
            text="Note : if you will use the Phone Paste the IP here",
            fill="#FFFFFF",
            font=("Inter Bold", 22 * -1)
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            460.0,
            152.0,
            image=entry_image_1
        )
        self.entry_1 = Entry(
            master=main_frame,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=297.0,
            y=122.0,
            width=326.0,
            height=58.0
        )

        # Create a style
        style = ttk.Style()
        style.configure('TButton', font=('Helvetica', 12))

        # Create a ttk.Button
        button_enter = ttk.Button(main_frame, text="Click Me", command=self.ip_Setter)
        button_enter.pack(pady=20)

        button_enter.place(
            x=700,
            y=140
        )

        #####
        result_label = ttk.Label(main_frame, textvariable=self.result_var)
        result_label.pack(pady=10)
        result_label.place(
            x=357.0,
            y=220
        )

        main_frame.image_refs = [button_image_1, button_image_2, button_image_3, button_image_4, button_image_5, entry_image_1]

# Example usage
# root = tk.Tk()
# main_frame = tk.Frame(root)
# back_frame = tk.Frame(root)
# save_frame = tk.Frame(root)
# gui = Gui()
# gui.camera_gui(root, main_frame, back_frame, save_frame)
# root.mainloop()

