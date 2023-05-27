try:
    from importt import *
except ModuleNotFoundError:
    try:
        from modules.importt import *
    except ModuleNotFoundError:
        from Engine.custom.modules.importt import *



def local_select_img():
    image_formats = [("JPEG", "*.jpg"),("PNG", "*.png")]
    file_path = filedialog.askopenfilename(filetypes=image_formats, title="Оберіть зображення")
    with open(os.path.join(PATH, "custom", "modules", "img.jpg"), "wb") as f:
        with open(file_path, "rb") as g:
            f.write(g.read())
    return_info = (file_path, info_and_resize_img(file_path))
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
        return return_info
    else:
        pass


def save_img():
    image_formates = [("JPEG", "*.jpg"),("PNG", "*.png")]
    file_path = os.path.join(PATH, "custom", "modules", "img.jpg")
    save_file = filedialog.asksaveasfile(filetypes = image_formates, title="Збережіть зображення")
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
    msg = f'''Назва світлини: {info[0]["Назва світлини"]}
    Вага світлини: {info[0]["Вага світлини"]}
    Висота світлини: {info[0]["Висота світлини"][0]}
    Ширина світлини: {info[0]["Ширина світлини"][0]}
    Формат світлини: {info[0]["Формат світлини"]}'''
    label = customtkinter.CTkLabel(master=menu, text=msg)
