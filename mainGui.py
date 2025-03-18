from DecoderGui import Gui
from SaveScene import save_Scene
from LocalFileScene import local_File_Scene
from Main_Scene import main_Scene
from FinalScene import final_Scene
from EditFileScene import edit_File_Scene
import tkinter as tk
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def main():
    window = tk.Tk()
    window.geometry("920x620")
    window.title("Innovation Area attendance system")
    window.resizable(False, False)
    window.configure(bg="#0E0E0E")
    # icon = tk.PhotoImage(file="assets\\image_1.png")
    # window.iconphoto(False, icon)

    # Create frames for each scene
    main_scene = tk.Frame(window)
    camera_scene = tk.Frame(window)
    file_scene = tk.Frame(window)
    save_scene = tk.Frame(window)
    final_scene = tk.Frame(window)
    edit_file_scene = tk.Frame(window)

    # Place all frames
    for frame in (main_scene, camera_scene, file_scene, save_scene, final_scene, edit_file_scene):
        frame.place(x=0, y=0, relwidth=1, relheight=1)

    # Initialize scenes
    main_Scene(main_frame=main_scene, camera_frame=camera_scene, file_frame=file_scene, edit_frame=edit_file_scene)
    camera = Gui()
    camera.camera_gui(window, main_frame=camera_scene, back_frame=main_scene, save_frame=save_scene)
    local_File_Scene(file_scene, back_frame=main_scene, save_frame=save_scene)
    edit_File_Scene(main_frame=edit_file_scene, back_frame=main_scene, save_frame=save_scene)
    save_Scene(main_frame=save_scene, final_frame=final_scene, back_frame=main_scene)
    final_Scene(final_scene)

    # Show the initial frame
    main_scene.tkraise()

    window.mainloop()

if __name__ == "__main__":
    main()
