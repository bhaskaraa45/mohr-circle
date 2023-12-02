import tkinter as tk
from tkinter import simpledialog

def get_user_input():
    root = tk.Tk()
    root.title("Mohr's Circle Input")

    tk.Label(root, text="Enter σx (Normal stress in X direction):").grid(row=0, column=0)
    sigma_x_entry = tk.Entry(root)
    sigma_x_entry.grid(row=0, column=1)

    tk.Label(root, text="Enter σy (Normal stress in Y direction):").grid(row=1, column=0)
    sigma_y_entry = tk.Entry(root)
    sigma_y_entry.grid(row=1, column=1)

    tk.Label(root, text="Enter τxy (Shear stress):").grid(row=2, column=0)
    tau_xy_entry = tk.Entry(root)
    tau_xy_entry.grid(row=2, column=1)

    tk.Label(root, text="Enter value of θ:").grid(row=3, column=0)
    angle_entry = tk.Entry(root)
    angle_entry.grid(row=3, column=1)

    def on_submit():
        global sigma_x, sigma_y, tau_xy, angle
        sigma_x = float(sigma_x_entry.get())
        sigma_y = float(sigma_y_entry.get())
        tau_xy = float(tau_xy_entry.get())
        angle = float(angle_entry.get())
        root.destroy()

    submit_button = tk.Button(root, text="Submit", command=on_submit)
    submit_button.grid(row=5, column=1)

    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    root.mainloop()

    return sigma_x, sigma_y, tau_xy, angle
