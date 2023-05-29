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
    file_path = os.path.join(PATH, "custom", "modules", "img.jpg")
    image_formats = [("JPEG", "*.jpg"),("PNG", "*.png")]
    save_file = filedialog.asksaveasfilename(filetypes=image_formats, title="Збережіть зображення", defaultextension=image_formats)
    img_open = Image.open(file_path)
    
    img_open.save(save_file)



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
    msg = f'''Назва світлини: {name};
    Вага світлини: {info[0]["Вага світлини"]} Kb;
    Висота світлини: {info[0]["Висота світлини"][0]};
    Ширина світлини: {info[0]["Ширина світлини"][0]};
    Формат світлини: {info[0]["Формат світлини"]}.'''
    label = customtkinter.CTkLabel(master = menu, text = msg, height = 175, width = 250, text_color="Black", text_font=(os.path.join(PATH, "custom", "modules", "angrybirds-regular3.ttf"), 13),)
    label.place(x=0,y=0)

# bl_w_w   mirr_w   blur_w
def colorist(info = os.path.join(PATH, "custom", "modules", "img2.jpg")):
    img_open = Image.open(info)
    img_open.save(os.path.join(PATH, "custom", "modules", "img3.jpg"))
    img_open = Image.open(os.path.join(PATH, "custom", "modules", "img3.jpg"))
    flag = False
    if bl_w_w.get():
        img_open = img_open.convert('L')
        img_open.save('Engine\custom\modules\img3.jpg')
        img_open = Image.open(os.path.join(PATH, "custom", "modules", "img3.jpg"))
        flag = True
    if mirr_w.get():
        img_open = img_open.transpose(Image.FLIP_LEFT_RIGHT)
        img_open.save(os.path.join(PATH, "custom", "modules", "img3.jpg"))
        img_open = Image.open(os.path.join(PATH, "custom", "modules", "img3.jpg"))
        flag = True
    if blur_w.get():
        img_open = img_open.filter(ImageFilter.BLUR)
        img_open.save(os.path.join(PATH, "custom", "modules", "img3.jpg"))
        img_open = Image.open(os.path.join(PATH, "custom", "modules", "img3.jpg"))
        flag = True
    if flag:
        ex.update_photo(os.path.join(PATH, "custom", "modules", "img3.jpg"))
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
