try:
    from modules.load_f import *
except:
    from Engine.custom.modules.load_f import *


menu.geometry("1280x720")
customtkinter.set_appearance_mode("System")
menu.title("Photoshopingist")
menu.iconbitmap(os.path.join(PATH,"custom","phot_icon.ico"))
menu["bg"] = "lightskyblue4"

# Меню
file_menu = tkinter.Menu(tearoff=0)
file_menu.add_command(label="Local File", command=local_select_img)
file_menu.add_command(label="URL FIle", command=web_select_img)
file_menu.add_command(label="Save FILE", command=save_img)
main_menu = tkinter.Menu()
main_menu.add_cascade(label="File", menu = file_menu)
menu.config(menu=main_menu)
menu.protocol("WM_DELETE_WINDOW", close_program)

bl_w = tkinter.Checkbutton(text="Чорно-білий",
                           variable=bl_w_w,
                           command = colorist,
                           width = 20,
                           height= 2,
                           font=(os.path.join(PATH, "custom", "modules", "angrybirds-regular3.ttf"), 13),
                           bg = "turquoise")
bl_w.pack(padx=6, pady=7, anchor="nw")
mirr = tkinter.Checkbutton(text="Відзеркалити",
                           variable=mirr_w,
                           command = colorist,
                           width = 20,
                           height= 2,
                           font=(os.path.join(PATH, "custom", "modules", "angrybirds-regular3.ttf"), 13),
                           bg = "turquoise")
mirr.pack(padx=6, pady=7, anchor="nw")
blur = tkinter.Checkbutton(text="Розмилення",
                           variable=blur_w,
                           command = colorist,
                           width = 20,
                           height= 2,
                           font=(os.path.join(PATH, "custom", "modules", "angrybirds-regular3.ttf"), 13),
                           bg = "turquoise")
blur.pack(padx=6, pady=7, anchor="nw")

# Отображение картинки
try:
    info_foto(info = info_and_resize_img(os.path.join(PATH, "custom", "modules", "img.png")))
except:
    pass



menu.mainloop()