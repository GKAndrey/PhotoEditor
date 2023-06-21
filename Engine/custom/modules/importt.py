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

PATH = os.path.abspath(__file__ + '/../../..')

class Ex():
    def __init__(self, master, size: list = (0,0), path = os.path.join(PATH, "custom", "modules", "img2.png"), flag = True):
        try:
            img_open = Image.open(path)
            w1 = img_open.width
            h1 = img_open.height
            while 1:
                if w1 > 900:
                    w1 = w1 // 2
                    h1 = h1 // 2
                    resize_for_txt[0] = resize_for_txt[0] * 2
                    resize_for_txt[1] = resize_for_txt[1] * 2
                elif w1 < 600:
                    w1 = w1 * 3
                    h1 = h1 * 3
                    resize_for_txt[0] = resize_for_txt[0] / 3
                    resize_for_txt[1] = resize_for_txt[1] / 3
                else:
                    break
            while h1 > 720:
                w1 = w1 // 2
                h1 = h1 // 2
            self.width = w1
            if size[0]:
                self.image = customtkinter.CTkImage(img_open, size = size)
            else:
                self.image = customtkinter.CTkImage(img_open, size = (w1, h1))
            self.image_sprite = customtkinter.CTkLabel(master=master,text = " ", image=self.image)
        except:
            self.image_sprite = tkinter.Label(menu)
        if flag:
            self.image_sprite.place(x = 1280-self.width, y=0)
        else:
            self.image_sprite.grid(column=0,row=0)
    def update_photo(self, path=os.path.join(PATH, "custom", "modules", "img2.png")):
        img_open = Image.open(path)
        w1 = img_open.width
        h1 = img_open.height
        while 1:
            if w1 > 900:
                w1 = w1 // 2
                h1 = h1 // 2
                resize_for_txt[0] = resize_for_txt[0] * 2
                resize_for_txt[1] = resize_for_txt[1] * 2
            elif w1 < 600:
                w1 = w1 * 3
                h1 = h1 * 3
                resize_for_txt[0] = resize_for_txt[0] / 3
                resize_for_txt[1] = resize_for_txt[1] / 3
            else:
                break
        while h1 > 720:
            w1 = w1 // 2
            h1 = h1 // 2
        self.image = customtkinter.CTkImage(img_open, size = (w1, h1))
        self.image_sprite.configure(image = self.image)
        self.width = w1
        self.image_sprite.place(x = 1280-self.width, y=0)
        

try:
    os.remove(os.path.join(PATH, "custom", "modules", "img3.png"))
except:
    pass
try:
    os.remove(os.path.join(PATH, "custom", "modules", "img4.png"))
except:
    pass
menu = customtkinter.CTk("lightskyblue4")

save_tk = 0
text_on_img_root = 0
crop_tk = 0
rotate = 0
resize_for_txt = [1,1]
txt_on_im = []
bl_w_w = tkinter.IntVar()
mirr_w = tkinter.IntVar()
blur_w = tkinter.IntVar()
w1, h1 = 0, 0