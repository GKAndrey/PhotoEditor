import PIL
from PIL.ExifTags import TAGS
from PIL import Image, ImageTk, ImageFilter, ImageDraw, ImageFont
import customtkinter
import os
import requests
import re
import tkinter
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import font
import time
import random


def info_and_resize_img(file_path):
    img_open = Image.open(file_path)
    img_resize = img_open.resize((720, 480))
    img_resize.save(os.path.join(PATH, "custom", "modules", "img2.png"))
    img_resize = Image.open(os.path.join(PATH, "custom", "modules", "img2.png"))
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
    def __init__(self, master, path = os.path.join(PATH, "custom", "modules", "img2.png"), flag = True):
        try:
            pil_image = Image.open(path)
            self.width = pil_image.width
            self.image = ImageTk.PhotoImage(pil_image)
            self.image_sprite = tkinter.Label(master=master, image=self.image)
        except:
            self.image_sprite = tkinter.Label(menu)
        if flag:
            self.image_sprite.place(x = 1280-self.width, y=0)
        else:
            self.image_sprite.grid(column=0,row=0)
    def update_photo(self, path=os.path.join(PATH, "custom", "modules", "img2.png")):
        pil_image = Image.open(path)
        self.image = ImageTk.PhotoImage(pil_image)
        self.image_sprite["image"] = self.image
        self.image_sprite.image = self.image
        self.width = pil_image.width
        self.image_sprite.place(x = 1280-self.width, y=0)

try:
    os.remove(os.path.join(PATH, "custom", "modules", "img3.png"))
except:
    pass
menu = tkinter.Tk()

save_tk = 0
text_on_img_root = 0
crop_tk = 0
rotate = 0
bl_w_w = tkinter.IntVar()
mirr_w = tkinter.IntVar()
blur_w = tkinter.IntVar()

try:
    ex = Ex(menu)
except:
    pass