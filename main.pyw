import tkinter as tk
from tkinter import ttk
import subprocess
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
ins_path = os.path.join(current_dir, "ins.pyw")
err_path = os.path.join(current_dir, "err.pyw")
man_path = os.path.join(current_dir, "man.pyw")

if not sys.platform.startswith('win'):
    subprocess.Popen(["python", err_path, "Please use Windows OS"], creationflags=subprocess.CREATE_NO_WINDOW)
    exit()

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def startupins():
    global buttonClicked
    buttonClicked = not buttonClicked
    subprocess.Popen(["python", ins_path])
    exit()

def startupman():
    global buttonClicked
    buttonClicked = not buttonClicked
    subprocess.Popen(["python", man_path])
    exit()

buttonClicked  = False # Before first click

window = tk.Tk()
window.title("BRMDB")  # Set the title of the window
window.configure(bg='#34A2FE')

greeting = tk.Label(window, text="Buckshot Roulette Mod Database GUI", background="#34A2FE", font=('Arial', 25), pady=20)
startupins_button = tk.Button(window, text="Start Installer", width=20, height=2, bg="#2467a0", fg="white", font=('Arial', 12, 'bold'), command=startupins)
startup_button = tk.Button(window, text="Start Mod Manager", width=20, height=2, bg="#2467a0", fg="white", font=('Arial', 12, 'bold'), command=startupman)

greeting.pack()
startupins_button.pack(pady=10)
startup_button.pack(pady=10)

window.mainloop()
