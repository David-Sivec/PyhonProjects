import tkinter as tk

root = tk.Tk()
root.title("Moja aplikácia")
root.geometry("300x400")

label = tk.Label(root, text="Zadaj číslo:")
label.pack()
entry = tk.Entry(root)
entry.pack()
def klik():
    print("Klik!")

button = tk.Button(root, text="Klikni", command=klik)
button.pack()
# Spustenie hlavnej slučky
root.mainloop()