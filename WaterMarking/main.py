import tkinter as tk
from PIL import ImageTk, Image,ImageDraw, ImageFont
from tkinter import filedialog

window = tk.Tk()
window.title("WaterMarking")

#window.geometry("550x300 + 300 + 150")

window.resizable(width = True, height = True)




def open_img():
    x = filedialog.askopenfilename(title="pen")
    img = Image.open(x)
    # resize the image and apply a high-quality down sampling filter
    img = img.resize((250, 250), Image.LANCZOS)
    d1 = ImageDraw.Draw(img)
    d1.text((65,10),"Sample Text", fill = (255,255,255))

    # PhotoImage class is used to add image to widgets, icons etc
    img = ImageTk.PhotoImage(img)

    # create a label
    panel = tk.Label(window, image=img)

    # set the image as img
    panel.image = img
    panel.grid(row=2)

btn = tk.Button(window, text="Open Image", command = open_img)
btn.grid(row = 1, columnspan = 4)
window.mainloop()