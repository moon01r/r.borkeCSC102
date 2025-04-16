import tkinter as tk
from tkinter import messagebox

def check_delivery_fee():
    user_location = loc_input.get().strip().lower()
    try:
        package_weight = float(weight_input.get())
    except ValueError:
        messagebox.showerror("Input Error", "Enter a valid number for weight.")
        return

    fee = None

    if user_location == "ibeju-lekki":
        fee = 5000 if package_weight >= 10 else 3500
    elif user_location == "epe":
        fee = 10000 if package_weight >= 10 else 5000
    else:
        messagebox.showerror("Unknown Area", "Only 'Ibeju-Lekki' and 'Epe' are supported.")
        return

    messagebox.showinfo("Result", f"Delivery cost: ₦{fee}")

# Set up the interface
app = tk.Tk()
app.title("Delivery Calculator")

tk.Label(app, text="Location (e.g. Ibeju-Lekki or Epe):").pack()
loc_input = tk.Entry(app)
loc_input.pack()

tk.Label(app, text="Weight (kg):").pack()
weight_input = tk.Entry(app)
weight_input.pack()

tk.Button(app, text="Check Price", command=check_delivery_fee).pack()

app.mainloop()