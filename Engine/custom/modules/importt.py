import PIL
from PIL.ExifTags import TAGS
from PIL import Image, ImageTk, ImageFilter
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

PATH = os.path.abspath(__file__ + '/../../..')

class Ex():
    def __init__(self):
        pil_image = Image.open(os.path.join(PATH, "custom", "modules", "img2.jpg"))
        self.image = ImageTk.PhotoImage(pil_image)
        self.image_sprite = tkinter.Label(menu, image=self.image)
        self.image_sprite.pack(anchor=tkinter.NE, expand=True)
    def update_photo(self, path=os.path.join(PATH, "custom", "modules", "img2.jpg")):
        pil_image = Image.open(path)
        self.image = ImageTk.PhotoImage(pil_image)
        self.image_sprite["image"] = self.image
        self.image_sprite.image = self.image


menu = tkinter.Tk()

bl_w_w = tkinter.IntVar()
mirr_w = tkinter.IntVar()
blur_w = tkinter.IntVar()

ex = Ex()