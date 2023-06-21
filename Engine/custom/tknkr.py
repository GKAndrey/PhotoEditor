try:
    from modules.load_f import *
except:
    from Engine.custom.modules.load_f import *


menu.geometry("1280x720")
menu.resizable(False, False)
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

none_l0 = tkinter.Label(menu, 
                        text = '',
                        bg = "lightskyblue4")
none_l0.grid(row = 1, column = 0, padx=6, pady=25, sticky="nw")

crop_b1 = tkinter.Button(master = menu,
                        text = 'Обрізка світлини',
                        width = 25,
                        height= 2,
                        command = pruning1,
                        bg = "PaleTurquoise3",
                        font = ("Helvetica", 12),
                        fg = "#191970")
crop_b1.grid(row = 2, column = 0, padx = 6, pady = 7, sticky="nw")

crop_b2 = tkinter.Button(master = menu,
                        text = 'Вставити текст на світлину',
                        width = 25,
                        height= 2,
                        command = text_on_img,
                        bg = "PaleTurquoise3",
                        fg = "#191970",
                        font = ("Helvetica", 12))
crop_b2.grid(row = 3, column = 0, padx=6, pady=7, sticky="nw")

none_l = tkinter.Label(master = menu,
                        text = '',
                        bg = "lightskyblue4")
none_l.grid(row = 4, column = 0, padx=6, pady=25, sticky="sw")

bl_w = tkinter.Checkbutton(master = menu,
                            text="Чорно-білий",
                            variable=bl_w_w,
                            command = colorist,
                            width = 20,
                            height= 2,
                            font=("Helvetica", 13),
                            bg = "PaleTurquoise3",
                            fg = "#191970",)
bl_w.grid(row = 5, column = 0, padx=6, pady=7, sticky="sw")
mirr = tkinter.Checkbutton(master = menu,
                            text="Відзеркалити",
                            variable=mirr_w,
                            command = colorist,
                            width = 20,
                            height= 2,
                            font=("Helvetica", 13),
                            bg = "PaleTurquoise3",
                            fg = "#191970")
mirr.grid(row = 6, column = 0, padx=6, pady=7, sticky="sw")
blur = tkinter.Checkbutton(master = menu,
                            text="Розмилення",
                            variable=blur_w,
                            command = colorist,
                            width = 20,
                            height= 2,
                            font=("Helvetica", 13),
                            bg = "PaleTurquoise3",
                            fg = "#191970",)
blur.grid(row = 7, column = 0, padx=6, pady=7, sticky="sw")

res_txt = customtkinter.CTkButton(master = menu,
                                text = "Видалити напис на зображеннi",
                                fg_color = ("PaleTurquoise3"),
                                text_color = "#191970",
                                font = ("Helvetica", 16),
                                command = res_txt_event,
                                width=120,
                                height=50,
                                border_width =  0,
                                corner_radius = 8)
res_txt.place(x=250, y = 357)

rotate_b1 = tkinter.Button(master = menu,
                        text = 'Перегорнути світлину ↪️',
                        width = 25,
                        height= 2,
                        command = rotate_img_left,
                        bg = "PaleTurquoise3",
                        fg = "#191970",
                        font = (os.path.join(PATH, "custom", "modules", "angrybirds-regular3.ttf"), 12))
rotate_b1.grid(row = 7, column = 1, padx = 6, pady = 7, sticky="nw")

rotate_b2 = tkinter.Button(master = menu,
                        font = (os.path.join(PATH, "custom", "modules", "angrybirds-regular3.ttf"), 12),
                        text = '↩️Перегорнути світлину',
                        width = 25,
                        height= 2,
                        command = rotate_img_right,
                        bg = "PaleTurquoise3",
                        fg = "#191970",)
rotate_b2.grid(row = 7, column = 2, padx=6, pady=7, sticky="nw")
# Отображение картинки
try:
    info_foto(info = info_and_resize_img(os.path.join(PATH, "custom", "modules", "img.png")))
except:
    pass



menu.mainloop()