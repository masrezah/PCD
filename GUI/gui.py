
import os
import tkinter.filedialog
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Label
from PIL import Image, ImageTk
from Feature.negativeImages import convert_to_negative
from Feature.grayscaleImages import convert_to_grayscale


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\00. Informatics Engineering\00. Matakuliah\01. SEM 5\06. PCD\PCD_UAS\assets\frame0")

file_name = None
file_path = None
img_label = None

def select_path():
    global file_path, img_label, image_3
    file_path = tkinter.filedialog.askopenfilename()
    file_name = os.path.basename(file_path)
    if file_path:
        img = Image.open(file_path)
        img = img.resize((600, 400), Image.LANCZOS)  # Resize the image to fit in the canvas
        img = ImageTk.PhotoImage(img)
        print(file_path)
        print(file_name)

        # Update the canvas
        canvas.itemconfig(file_name_text, text = file_name)

        # Update image_3 with the selected image
        if img_label is None:
            img_label = Label(window, image=img)
            img_label.image = img
            img_label.place(x=506, y=206)  # Adjust position as needed
        else:
            img_label.config(image=img)
            img_label.image = img

def reset_path():
    global file_path, file_name, img_label
    file_path = None
    file_name = None

    # Update
    canvas.itemconfig(file_name_text, text = "")

    if img_label:
        img_label.place_forget()
        img_label = None

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



window = Tk()
window.geometry("1600x800")
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 800,
    width = 1600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1600.0,
    800.0,
    fill="#E7F0DC",
    outline=""
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    800.0,
    41.0,
    image=image_image_1
)

button_image_close = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_reset_file = Button(
    image=button_image_close,
    borderwidth=0,
    highlightthickness=0,
    command=reset_path,
    relief="flat"
)
button_reset_file.place(
    x=1521.0,
    y=19.0,
    width=43.0,
    height=43.0
)

button_image_select = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_select = Button(
    image=button_image_select,
    borderwidth=0,
    highlightthickness=0,
    command=select_path,
    relief="flat"
)
button_select.place(
    x=1402.0,
    y=20.0,
    width=110.0,
    height=41.0
)

button_negativeImage = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_negative = Button(
    image=button_negativeImage,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: convert_to_negative(file_path), # Memanggil fungsi
    relief="flat"
)
button_negative.place(
    x=44.0,
    y=717.0,
    width=169.0,
    height=55.0
)

button_grayscaleImage = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_grayscale = Button(
    image=button_grayscaleImage,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: convert_to_grayscale(file_path),
    relief="flat"
)
button_grayscale.place(
    x=234.0,
    y=717.0,
    width=169.0,
    height=55.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=424.0,
    y=717.0,
    width=169.0,
    height=55.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=994.0,
    y=717.0,
    width=169.0,
    height=55.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=1184.0,
    y=717.0,
    width=169.0,
    height=55.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=804.0,
    y=717.0,
    width=169.0,
    height=55.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=614.0,
    y=717.0,
    width=169.0,
    height=55.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=1374.0,
    y=717.0,
    width=191.000244140625,
    height=55.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    274.0,
    41.0,
    image=image_image_2
)

canvas.create_text(
    41.0,
    24.0,
    anchor="nw",
    text="ImageNation",
    fill="#FFFFFF",
    font=("Montserrat Bold", 28 * -1)
)

canvas.create_text(
    35.0,
    90.0,
    anchor="nw",
    text="File name :",
    fill="#445A34",
    font=("Montserrat Bold", 24 * -1)
)

file_name_text = canvas.create_text(
    189.0,
    90.0,
    anchor="nw",
    text="",
    fill="#445A34",
    font=("Montserrat Bold", 24 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    806.0,
    406.0,
    image=image_image_3
)

window.resizable(True, True)
window.mainloop()

