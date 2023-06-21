try:
    from modules.load_f import *
except:
    from Engine.custom.modules.load_f import *


menu.geometry("1280x720")
menu.resizable(False, False)
customtkinter.set_appearance_mode("System")
menu.title("Photoshopingist")
menu.iconbitmap(os.path.join(PATH,"custom","phot_icon.ico"))

try:
    info_and_resize_img()
    ex = Ex(menu, (w1, h1))
except:
    pass

# Меню
file_menu = tkinter.Menu(tearoff=0)
file_menu.add_command(label="Local File", command=local_select_img)
file_menu.add_command(label="URL FIle", command=web_select_img)
file_menu.add_command(label="Save FILE", command=save_img)
main_menu = tkinter.Menu()
main_menu.add_cascade(label="File", menu = file_menu)
menu.config(menu=main_menu)
menu.protocol("WM_DELETE_WINDOW", close_program)

none_l0 = customtkinter.CTkLabel(menu, 
                        text = '',
                        width=300,
                        height=50,
                        fg_color = "lightskyblue4")
none_l0.grid(row = 1, column = 0,  padx=18, pady=15, sticky="nw")

crop_b1 = customtkinter.CTkButton(master = menu,
                        text = 'Обрізка світлини',
                        width=300,
                        height=50,
                        command = pruning1,
                        text_color = "#191970",
                        font = ("Helvetica", 16),
                        fg_color = ("PaleTurquoise3"))
crop_b1.grid(row = 2, column = 0, padx=18, pady=7, sticky="nw")

crop_b2 = customtkinter.CTkButton(master = menu,
                        text = 'Вставити текст на світлину',
                        width=300,
                        height=50,
                        command = text_on_img,
                        fg_color = ("PaleTurquoise3"),
                        text_color = "#191970",
                        font = ("Helvetica", 16))
crop_b2.grid(row = 3, column = 0,  padx=18, pady=7, sticky="nw")

none_l = customtkinter.CTkLabel(master = menu,
                        text = '',
                        width=300,
                        height=50,
                        fg_color = "lightskyblue4")
none_l.grid(row = 4, column = 0,  padx=18, pady=25, sticky="sw")

bl_w = customtkinter.CTkCheckBox(master = menu,
                            text="Чорно-білий",
                            variable=bl_w_w,
                            command = colorist,
                            width = 20,
                            height=50,
                            font=("Helvetica", 13),
                            fg_color = "#191970",)
bl_w.grid(row = 5, column = 0,  padx=18, pady=7, sticky="sw")
mirr = customtkinter.CTkCheckBox(master = menu,
                            text="Відзеркалити",
                            variable=mirr_w,
                            command = colorist,
                            width = 20,
                            height=50,
                            font=("Helvetica", 13),
                            fg_color = "#191970")
mirr.grid(row = 6, column = 0,  padx=18, pady=7, sticky="sw")
blur = customtkinter.CTkCheckBox(master = menu,
                            text="Розмилення",
                            variable=blur_w,
                            command = colorist,
                            width = 20,
                            height=50,
                            font=("Helvetica", 13),
                            fg_color = "#191970",)
blur.grid(row = 7, column = 0,  padx=18, pady=7, sticky="sw")

res_txt = customtkinter.CTkButton(master = menu,
                                text = '''Видалити напис 
на зображеннi''',
                                fg_color = ("PaleTurquoise3"),
                                text_color = "#191970",
                                font = ("Helvetica", 16),
                                command = res_txt_event,
                                width=150,
                                height=50,
                                border_width =  0,
                                corner_radius = 8)
res_txt.grid(row = 3, column = 1,  padx=18, pady=7, sticky="nw")

rotate_b1 = customtkinter.CTkButton(master = menu,
                        text = 'Перегорнути світлину ↪️',
                        width=300,
                        height=50,
                        command = rotate_img_left,
                        fg_color = ("PaleTurquoise3"),
                        text_color = "#191970",
                        font = ("Helvetica", 16))
rotate_b1.grid(row = 7, column = 1, padx = 6, pady = 7, sticky="nw")

rotate_b2 = customtkinter.CTkButton(master = menu,
                        text = '↩️Перегорнути світлину',
                        width=300,
                        height=50,
                        command = rotate_img_right,
                        fg_color = ("PaleTurquoise3"),
                        text_color = "#191970",
                        font = ("Helvetica", 16))
rotate_b2.grid(row = 7, column = 2,  padx=18, pady=7, sticky="nw")

# Отображение картинки
try:
    info_foto(info = info_and_resize_img(os.path.join(PATH, "custom", "modules", "img.png")))
except:
    pass



menu.mainloop()