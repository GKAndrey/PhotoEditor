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
        except:
            img = requests.get("https://" + URL_img)
        file_path = os.path.join(PATH, "custom", "modules", "img.png")
        with open(file_path, "wb") as f:
            f.write(img.content)
        return_info = [file_path, info_and_resize_img(file_path)]
        ex.update_photo()
        return return_info
    else:
        pass



def save_img():
    global save_tk, btn_save, save_file_v, save_input
    def save_file():
        global save_path
        save_path = save_input.get()
        if save_path:
            try:
                colorist(os.path.join(PATH, "custom", "modules", "img.png"), False)
                img_open = Image.open(os.path.join(PATH, "custom", "modules", "img3.png"))
                img_open.save(save_path)
            except ValueError:
                messagebox.showerror("Критична помилка!", "Помилковий тип файлу!")
            except FileNotFoundError:
                messagebox.showerror("Критична помилка!", "Обраний шлях не існує!")
            finally:
                save_input.focus()
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
    save_tk.geometry("400x200")
    save_tk.title("Збереження фото")
    save_tk.iconbitmap(os.path.join(PATH,"custom","phot_icon.ico"))
    save_tk["bg"] = "gray58"
    save_input = tkinter.Entry(save_tk, width=50, font=(os.path.join(PATH, "custom", "modules", "angrybirds-regular3.ttf"), 12))
    save_input.pack(pady=10)
    save_input.focus()
    btn_save = tkinter.Button(master = save_tk,text="Зберегти", width = 30, command=save_file, font=(os.path.join(PATH, "custom", "modules", "angrybirds-regular3.ttf"), 12))
    btn_save.pack(side="bottom", pady=3)
    btn_save_path = tkinter.Button(master = save_tk,text="Обрати шлях на комп'ютері", width = 30, command=save_file_Path, font=(os.path.join(PATH, "custom", "modules", "angrybirds-regular3.ttf"), 12))
    btn_save_path.pack(side="top", pady=7)
    save_tk.mainloop()



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



def info_foto(info):
    name = info[0]["Назва світлини"].split("\\")[-1]
    msg = f'''Назва світлини: {name};
    Вага світлини: {info[0]["Вага світлини"]} Kb;
    Висота світлини: {info[0]["Висота світлини"][0]};
    Ширина світлини: {info[0]["Ширина світлини"][0]};
    Формат світлини: {info[0]["Формат світлини"]}.'''
    label = customtkinter.CTkLabel(master = menu, text = msg, height = 175, width = 250, text_color="Black", text_font=(os.path.join(PATH, "custom", "modules", "angrybirds-regular3.ttf"), 13),)
    label.place(x=0,y=0)

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
        img_open = img_open.filter(ImageFilter.BLUR)
        img_open.save(os.path.join(PATH, "custom", "modules", "img3.png"))
        img_open = Image.open(os.path.join(PATH, "custom", "modules", "img3.png"))
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

def change_res(info = os.path.join(PATH, "custom", "modules", "img2.png")):
    res_w = tkinter.Tk()
    res_w.geometry("400x150")
    res_w.title("Зміна роздільної здатності")
    res_w.iconbitmap(os.path.join(PATH,"custom","phot_icon.ico"))
    res_w["bg"] = "gray58"

    input_res = tkinter.Entry(res_w)
    input_res.pack(side = "top", anchor='ne')
    res = input_res.get()
    pattern = re.match(r'([0-9]+)', res)

    res_w.mainloop()