import PIL
from PIL.ExifTags import TAGS
from PIL import Image, ImageTk
import customtkinter
import os
import requests
import tkinter
from tkinter import ttk
from tkinter import filedialog
import time


def info_and_resize_img(file_path):
    img_open = Image.open(file_path)
    img_resize = img_open.resize((720, 480))
    img_resize.save(os.path.join(PATH, "custom", "modules", "img2.jpg"))
    img_resize = Image.open(os.path.join(PATH, "custom", "modules", "img2.jpg"))
    img_info = {
        "Назва світлини": img_open.filename,
        "Вага світлини": os.path.getsize(file_path) // 1024,
        "Висота світлини": [img_open.height, img_resize.height],
        "Ширина світлини": [img_open.width, img_resize.width],
        "Формат світлини": img_open.format,
        }
    return_info = [img_info, img_resize]
    return return_info


class Example(tkinter.Frame):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.img = Image.open(os.path.join(PATH, "custom", "modules", "img2.jpg"))
        self.image = ImageTk.PhotoImage(self.img)
        self.info = info_and_resize_img(os.path.join(PATH, "custom", "modules", "img2.jpg"))
        canvas = tkinter.Canvas(
            height=self.info[0]["Висота світлини"][1],
            width=self.info[0]["Ширина світлини"][1]
        )
        canvas.create_image(0, 0, anchor=tkinter.NE, image=self.image)
        canvas.pack(anchor=tkinter.NE, expand=True)

class Ex():
    def __init__(self):
        pil_image = Image.open(os.path.join(PATH, "custom", "modules", "img2.jpg"))
        self.image = ImageTk.PhotoImage(pil_image)
        image_sprite = tkinter.Label(menu, image=self.image)
        image_sprite.pack(anchor=tkinter.NE, expand=True)



PATH = os.path.abspath(__file__ + '/../../..')

menu = tkinter.Tk()

ex = Ex()