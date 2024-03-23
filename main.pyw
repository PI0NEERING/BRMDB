import tkinter as tk
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

def check_xdelta3():
    try:
        subprocess.check_call(["xdelta3", "--version"])
        print("xdelta3 is already installed on the system.")
    except FileNotFoundError:
        print("xdelta3 is not installed. Installing...")
        install("xdelta3")
        print("xdelta3 has been successfully installed.")

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def startupins():
    global buttonClicked
    buttonClicked = not buttonClicked
    subprocess.Popen(["python", ins_path], creationflags=subprocess.CREATE_NO_WINDOW)
    exit()

def startupman():
    global buttonClicked
    buttonClicked = not buttonClicked
    subprocess.Popen(["python", man_path], creationflags=subprocess.CREATE_NO_WINDOW)
    exit()

check_xdelta3()

buttonClicked  = False # Before first click

window = tk.Tk()
window.title("BRMDB")  # Set the title of the window

greeting = tk.Label(text="Buckshot Roulette Mod Database GUI", background="#34A2FE", font=('Arial', 25))
startupins_button = tk.Button(text="Start installer", width=25, height=5, bg="#2467a0", command=startupins)
startup_button = tk.Button(text="Start mod manager", width=25, height=5, bg="#2467a0", command=startupman)

greeting.pack()
startupins_button.pack()
startup_button.pack()

window.mainloop()
