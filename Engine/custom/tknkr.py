import tkinter
import customtkinter
import os

PATH = os.path.abspath(__file__ + '/..')

menu = tkinter.Tk()
menu.geometry("1600x900")
customtkinter.set_appearance_mode("System")
menu.title("Photoshopingist")
menu.iconbitmap(os.path.join(PATH,"phot_icon.ico"))
menu["bg"] = "gray22"





menu.mainloop()