try:
    from modules.load_f import *
except:
    from Engine.custom.modules.load_f import *


menu.geometry("1280x720")
customtkinter.set_appearance_mode("System")
menu.title("Photoshopingist")
menu.iconbitmap(os.path.join(PATH,"custom","phot_icon.ico"))
menu["bg"] = "gray22"

# Меню
file_menu = tkinter.Menu(tearoff=0)
file_menu.add_command(label="Local File", command=local_select_img)
file_menu.add_command(label="URL FIle", command=web_select_img)
file_menu.add_command(label="Save FILE", command=save_img)
main_menu = tkinter.Menu()
main_menu.add_cascade(label="File", menu = file_menu)
menu.config(menu=main_menu)

# label1 = ctk.CTkLabel(master=menu,
#                       text=f"Назва світлини: {return_info[0]["Назва світлини"]}")
# label2 = ctk.CTkLabel(master=menu,
#                       text=f"Вага світлини: {return_info[0]["Вага світлини"]}")
# label3 = ctk.CTkLabel(master=menu,
#                       text=f"Висота світлини: {return_info[0]["Висота світлини"][0]}")
# label4 = ctk.CTkLabel(master=menu,
#                       text=f"Ширина світлини: {return_info[0]["Ширина світлини"][0]}")
# label5 = ctk.CTkLabel(master=menu,
#                       text=f"Формат світлини: {return_info[0]["Формат світлини"]}",)

# Отображение картинки
try:
    # imag = info_and_resize_img(os.path.join(PATH, "custom", "modules", "img2.jpg"))
    # canvas = tkinter.Canvas(menu, height=imag[0]["Висота світлини"][1], width=imag[0]["Ширина світлини"][1], bg = "Black")
    # image = Image.open(imag[0]["Назва світлини"])
    # photo = ImageTk.PhotoImage(image)
    # canvas.create_image(0, 0, anchor=tkinter.NW,image=photo)
    # canvas.pack(anchor=tkinter.NE, expand=True)
    info_foto(info = info_and_resize_img(os.path.join(PATH, "custom", "modules", "img.jpg")))
except:
    pass



menu.mainloop()