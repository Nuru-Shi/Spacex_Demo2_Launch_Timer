import tkinter as tk
from datetime import datetime
import time

WIDTH, HEIGHT = 1000, 250

def destroybutton():
    button.destroy()

def timer():
    space_x = datetime(2020, 5, 30, 21 - 1, 22, 0).timestamp()
    delta = space_x - time.time()

    if delta >= 0:
        label["text"] = time.strftime("%H:%M:%S", time.localtime(delta)) + " until demo-2 launch!"

        root.after(1000, timer)

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

black_image = tk.PhotoImage(file="pluscolorblack.png")
black_label = tk.Label(root, image=black_image)
black_label.place(x=0, y=0, relwidth=1, relheight=1)

background_image = tk.PhotoImage(file="spacex.png")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=50, relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#808080", bd=20)
frame.place(relwidth=0.6, relheight=0.4, relx=0.2, rely=0.1)

label = tk.Label(frame, font=("sans serif", "24", "bold"))
label.place(relwidth=1, relheight=1)

button = tk.Button(frame, text="See timer!", font=("Arial", "15", "bold"), command=lambda: [timer(), destroybutton()])
button.place(relheight=1, relwidth=1)

root.mainloop()