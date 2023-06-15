try:
    from importt import *
except ModuleNotFoundError:
    try:
        from modules.importt import *
    except ModuleNotFoundError:
        from Engine.custom.modules.importt import *



def close_program():
    menu.destroy()
    try:
        save_tk.destroy()
    except:
        pass

def local_select_img():
    image_formats = [("Зображення", "*.jpg;*.jpeg;*.png")]
    file_path = filedialog.askopenfilename(filetypes=image_formats, title="Оберіть зображення")
    with open(os.path.join(PATH, "custom", "modules", "img.png"), "wb") as f:
        try:
            with open(file_path, "rb") as g:
                f.write(g.read())
            return_info = (file_path, info_and_resize_img(file_path))
            ex.update_photo()
            return return_info
        except FileNotFoundError:
            pass


def web_select_img():
    dialog = customtkinter.CTkDialog(text="Введіть URL зображення:", title="Оберіть зображення")
    URL_img = dialog.get_input()
    if URL_img != '':
        try:
            img = requests.get(URL_img)
            file_path = os.path.join(PATH, "custom", "modules", "img.png")
            with open(file_path, "wb") as f:
                f.write(img.content)
            return_info = [file_path, info_and_resize_img(file_path)]
            ex.update_photo()
            return return_info
        except:
            try:
                img = requests.get("https://" + URL_img)
                file_path = os.path.join(PATH, "custom", "modules", "img.png")
                with open(file_path, "wb") as f:
                    f.write(img.content)
                return_info = [file_path, info_and_resize_img(file_path)]
                ex.update_photo()
                return return_info
            except:
                pass
    else:
        messagebox.showerror("Критична помилка!", "URL Адресса відсутня!")



def save_img():
    global save_tk, btn_save, save_file_v, save_input, input_res, btn_res_preview
    def save_file():
        global save_path
        save_path = save_input.get()
        if save_path:
            try:
                colorist(os.path.join(PATH, "custom", "modules", "img.png"), False)
                if input_res.get() != "":
                    resolution_get(os.path.join(PATH, "custom", "modules", "img3.png"))
                    img_open = Image.open(os.path.join(PATH, "custom", "modules", "img4.png"))
                else:
                    img_open = Image.open(os.path.join(PATH, "custom", "modules", "img3.png"))
                img_open.save(save_path)
            except ValueError:
                messagebox.showerror("Критична помилка!", "Помилковий тип файлу!")
            except FileNotFoundError:
                messagebox.showerror("Критична помилка!", "Обраний шлях не існує!")
            finally:
                save_input.focus()
        else:
            vv = random.randint(0, 100)
            if vv == 1:
                messagebox.showerror("Святая инквизиция!", "Згинь нечесть лютая! Задолбали пытаться меня сломать!!!")
            else:
                messagebox.showerror("Критична помилка!", "Обраний шлях не існує!")
    def save_file_Path():
        global save_path, save_input
        image_formats = [("JPEG", "*.jpg"),("PNG", "*.png")]
        save_path = filedialog.asksaveasfilename(filetypes=image_formats, title="Збережіть зображення", defaultextension=image_formats)
        save_input.delete(0, last=tkinter.END)
        save_input.insert(0, save_path)
    def close_window():
        save_path = None
        save_tk.destroy()
    file_path = os.path.join(PATH, "custom", "modules", "img.png")
    save_tk = tkinter.Tk()
    save_tk.protocol("WM_DELETE_WINDOW", close_window)
    save_tk.geometry("640x130")
    save_tk.title("Збереження фото")
    save_tk.iconbitmap(os.path.join(PATH,"custom","phot_icon.ico"))
    save_tk["bg"] = "gray58"

    save_input = tkinter.Entry(save_tk,
                               width=35,
                               font=(os.path.join(PATH, "custom", "modules", "angrybirds-regular3.ttf"), 12))
    save_input.grid(row=0, column=0, sticky='w', pady=5, padx=10)
    save_input.focus()

    input_res = tkinter.Entry(save_tk,
                              width=35,
                              font=(os.path.join(PATH, "custom", "modules", "angrybirds-regular3.ttf"), 12))
    input_res.grid(row=1, column=0, sticky='w', pady=5, padx=10)

    btn_save_path = tkinter.Button(save_tk,
                                   text = "Обрати шлях на комп'ютері",
                                   width = 30,
                                   command = save_file_Path,
                                   font = (os.path.join(PATH, "custom", "modules", "angrybirds-regular3.ttf"), 12))
    btn_save_path.grid(row=0, column=1, pady=5, padx=10)

    btn_res = tkinter.Button(save_tk,
                             text='Змінити роздільну здатність',
                             width=30,
                             command=resolution_get,
                             font=(os.path.join(PATH, "custom", "modules", "angrybirds-regular3.ttf"), 12))
    btn_res.grid(row=1, column=1, pady=5, padx=10)

    btn_res_preview = tkinter.Button(save_tk,
                                     text='Переглянути результат маcштабування',
                                     width= 35,
                                     command=resolution_preview,
                                     font=(os.path.join(PATH, "custom", "modules", "angrybirds-regular3.ttf"), 12))
    btn_res_preview.config(state='disabled')
    btn_res_preview.grid(row=2, column=0, pady=5, padx=9)

    btn_save = tkinter.Button(save_tk,
                              text="Зберегти",
                              width = 30,
                              command=save_file,
                              font=(os.path.join(PATH, "custom", "modules", "angrybirds-regular3.ttf"), 12))
    btn_save.grid(row=2, column=1, pady=5, padx=10)
    
    save_tk.mainloop()



def info_and_resize_img(file_path):
    img_open = Image.open(file_path)
    w1 = img_open.width
    h1 = img_open.height
    while w1 > 800:
        w1 = w1 // 2
        h1 = h1 // 2
    while h1 > 720:
        w1 = w1 // 2
        h1 = h1 // 2
    img_resize = img_open.resize((w1, h1))
    img_resize.save(os.path.join(PATH, "custom", "modules", "img2.png"))
    img_resize = Image.open(os.path.join(PATH, "custom", "modules", "img2.png"))
    img_info = {
        "Назва світлини": img_open.filename,
        "Вага світлини": os.path.getsize(file_path) // 1024,
        "Висота світлини": [img_open.height, img_resize.height],
        "Ширина світлини": [img_open.width, img_resize.width],
        "Формат світлини": img_open.format
        }
    return_info = [img_info, img_resize]
    info_foto(return_info)
    return return_info



def info_foto(info):
    if "\\" in info[0]["Назва світлини"]:
        name = info[0]["Назва світлини"].split("\\")[-1]
    else:
        name = info[0]["Назва світлини"].split("/")[-1]
    msg = f'''Назва світлини: {name};
    Вага світлини: {info[0]["Вага світлини"]} Kb;
    Висота світлини: {info[0]["Висота світлини"][0]};
    Ширина світлини: {info[0]["Ширина світлини"][0]};
    Формат світлини: {info[0]["Формат світлини"]}.'''
    label = customtkinter.CTkLabel(master = menu,
                                   text = msg,
                                   height = 175,
                                   width = 250,
                                   text_color="Black",
                                   text_font=(os.path.join(PATH, "custom", "modules", "angrybirds-regular3.ttf"), 13),)
    label.grid(row = 0, column = 0, padx=7, pady=20,  sticky="nw")

# bl_w_w   mirr_w   blur_w
def colorist(info = os.path.join(PATH, "custom", "modules", "img2.png"), flg = 1):
    img_open = Image.open(info)
    img_open.save(os.path.join(PATH, "custom", "modules", "img3.png"))
    img_open = Image.open(os.path.join(PATH, "custom", "modules", "img3.png"))
    flag = False
    if bl_w_w.get():
        img_open = img_open.convert('L')
        img_open.save(os.path.join(PATH, "custom", "modules", "img3.png"))
        img_open = Image.open(os.path.join(PATH, "custom", "modules", "img3.png"))
        flag = True
    if mirr_w.get():
        img_open = img_open.transpose(Image.FLIP_LEFT_RIGHT)
        img_open.save(os.path.join(PATH, "custom", "modules", "img3.png"))
        img_open = Image.open(os.path.join(PATH, "custom", "modules", "img3.png"))
        flag = True
    if blur_w.get():
        img_open = img_open.filter(PIL.ImageFilter.BLUR)
        img_open.save(os.path.join(PATH, "custom", "modules", "img3.png"))
        img_open = Image.open(os.path.join(PATH, "custom", "modules", "img3.png"))
        flag = True
    if rotate != 0:
        img_open = Image.open(os.path.join(PATH, "custom", "modules", "img3.png"))
        img_open = img_open.rotate(rotate)
        img_open.save(os.path.join(PATH, "custom", "modules", "img3.png"))
        flag = True
    if flg:
        if flag:
            ex.update_photo(os.path.join(PATH, "custom", "modules", "img3.png"))
        else:
            ex.update_photo()

    # ImageFilter.BoxBlur()

def convertor(info, name, format):
    img_open = Image.open(info[0])
    if format == 1:
        img_open.save(f"{name}.png", "PNG")
    elif format == 2:
        img_open.save(f"{name}.jpeg", "JPEG")
    elif format == 3:
        img_open.save(f"{name}.jpg", "JPG")


def resolution_get(info = os.path.join(PATH, "custom", "modules", "img.png")):
    global res_pattern, btn_res_preview
    res_pattern = re.findall(r'([0-9]+)', input_res.get())
    if input_res.get() != '':
        pos1 = int(res_pattern[0])
        pos2 = int(res_pattern[1])
    img_open = Image.open(info)
    try:
        res_img = img_open.resize((pos1, pos2))
        res_img.save(os.path.join(PATH, "custom", "modules", "img4.png"), "PNG")
        btn_res_preview.config(state='normal')
    except AttributeError:
        messagebox.showerror("Критична помилка!", "Помилкa вводу розміру!")


def resolution_preview(info = os.path.join(PATH, "custom", "modules", "img4.png")):
    res_img = Image.open(os.path.join(PATH, "custom", "modules", "img4.png"))
    res_w = tkinter.Tk()
    res_w.geometry(f"{res_img.size[0] + 10}"+'x'+f"{res_img.size[1] + 10}")
    res_w.title("Зміна роздільної здатності")
    res_w.iconbitmap(os.path.join(PATH,"custom","phot_icon.ico"))
    res_w["bg"] = "gray58"
    resized_image = ImageTk.PhotoImage(Image.open(os.path.join(PATH, "custom", "modules", "img4.png")), master = res_w)
    res_view = tkinter.Label(res_w,image=resized_image)
    res_view.pack()
    btn_res_preview.config(state='disabled')
    res_w.mainloop()

def pruning1():
    crop_img = Image.open(os.path.join(PATH, "custom", "modules", "img.png"))
    crop_tk = tkinter.Tk()
    crop_tk.geometry(f"{crop_img.size[0]}x{crop_img.size[1]}")
    crop_tk.title("Оберiть область вирiзу, перемiстив позначки")
    crop_tk.iconbitmap(os.path.join(PATH,"custom","phot_icon.ico"))
    crop_tk.resizable(False, False)
    crop_tk["bg"] = "gray58"
    resized_image = ImageTk.PhotoImage(crop_img, master = crop_tk)
    res_view = tkinter.Label(crop_tk,image=resized_image)
    res_view.place(x=0,y=0)
    
    pos1 = tkinter.Button(master = crop_tk, text = "1", font = ("Helvetica", 12), bg = "Black", fg = "white", width = 1, height = 1)
    pos1.place(x=0, y=0)
    
    pos2 = tkinter.Button(master = crop_tk, text = "2", font = ("Helvetica", 12), bg = "Black", fg = "white", width = 1, height = 1)
    pos2.place(x=crop_img.size[0]-100, y=crop_img.size[1]-100)
    
    safe_crop = tkinter.Button(master = crop_tk, text = "Зберегти", font = ("Helvetica", 12), bg = "Black", fg = "white", width = 10, height = 1)
    safe_crop.place(x=crop_img.size[0]-100, y=0)
    
    crop_tk.mainloop()

def rotate_img_left(info = os.path.join(PATH, "custom", "modules", "img3.png")):
    global rotate
    if rotate == 0:
        rotate = 90
    else:
        rotate += 90
    colorist()

def rotate_img_right(info = os.path.join(PATH, "custom", "modules", "img3.png")):
    global rotate
    if rotate == 0:
        rotate = 270
    else:
        rotate -= 90
    colorist()

# color = (255,0,0)
# def text_on_img(x, y, text, color, font = ImageFont.truetype("arial", size=50), info = os.path.join(PATH, "custom", "modules", "img3.png")):
#     global text_img_prev, text_img_prev1, img_opens3, text_img_tk
#     img_opens3 = Image.open(info)

#     text_img_tk = tkinter.Tk()
#     text_img_tk.geometry(f"{img_opens3.size[0] +50}x{img_opens3.size[1] + 10}")
#     text_img_tk.title("Вставлення тексту")
#     text_img_tk.iconbitmap(os.path.join(PATH,"custom","phot_icon.ico"))
#     text_img_tk["bg"] = "gray58"
    
#     text_write = ImageDraw.Draw(img_opens3)
#     text_write.text((x, y), text, font = font, fill = color)
    
#     ex9 = Ex(text_img_tk, info, False)
    
#     text_img_tk.mainloop()
    
# text_on_img(0,0, "hei tostyc", color)