try:
    from importt import *
except ModuleNotFoundError:
    try:
        from modules.importt import *
    except ModuleNotFoundError:
        from Engine.custom.modules.importt import *



def local_select_img():
    file_types = ("Image Files", "*.jpg;*.jpeg;*.png")
    file_path = filedialog.askopenfilename(filetypes=file_types, title="Оберіть зображення")
    with open(os.path.join(PATH, "custom", "modules", "img.jpg"), "wb") as f:
        with open(file_path, "rb") as g:
            f.write(g.read())
    return_info = (file_path, info_and_resize_img(file_path))
    ex.update_photo()
    return return_info


def web_select_img():
    dialog = customtkinter.CTkDialog(text="Введіть URL зображення:", title="Оберіть зображення")
    URL_img = dialog.get_input()
    if URL_img != '':
        try:
            img = requests.get(URL_img)
        except:
            img = requests.get("https://" + URL_img)
        file_path = os.path.join(PATH, "custom", "modules", "img.jpg")
        with open(file_path, "wb") as f:
            f.write(img.content)
        return_info = [file_path, info_and_resize_img(file_path)]
        ex.update_photo()
        return return_info
    else:
        pass



def save_img():
    file_types = ("Image Files", "*.jpg;*.jpeg;*.png")
    file_path = os.path.join(PATH, "custom", "modules", "img.jpg")
    save_file = filedialog.asksaveasfile(filetypes=file_types, title="Збережіть зображення")
    with open(save_file, "wb") as f:
        with open(file_path, "rb") as g:
            f.write(g)



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



def info_foto(info):
    name = info[0]["Назва світлини"].split("\\")[-1]
    msg = f'''Назва світлини: {name}
    Вага світлини: {info[0]["Вага світлини"]}
    Висота світлини: {info[0]["Висота світлини"][0]}
    Ширина світлини: {info[0]["Ширина світлини"][0]}
    Формат світлини: {info[0]["Формат світлини"]}'''
    label = customtkinter.CTkLabel(master = menu, text = msg, height = 175, width = 250)
    label.place(x=0,y=0)



def bw(file_path):
    img_open = Image.open(file_path)
    img_bw = img_open.convert('L')
    img_bw.save('Engine\custom\modules\img_bw.png')

def miror(file_path):
    img_open = Image.open(file_path)
    img_mir = img_open.transpose(Image.FLIP_LEFT_RIGHT)
    img_mir.save('Engine\custom\modules\img_mirored.png')

def convertor(file_path, name, format):
    img_open = Image.open(file_path)
    if format == 1:
        img_open.save(f"{name}.png", "PNG")
    elif format == 2:
        img_open.save(f"{name}.jpeg", "JPEG")
    elif format == 3:
        img_open.save(f"{name}.jpg", "JPG")