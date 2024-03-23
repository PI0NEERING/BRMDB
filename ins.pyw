import tkinter as tk
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def startupins():
    global buttonClicked
    buttonClicked = not buttonClicked
    exit()

buttonClicked  = False # Bfore first click

window = tk.Tk()
greeting = tk.Label(text="Buckshot Roulette Mod Database GUI", background="#34A2FE", font=('Arial', 25))
startupins = tk.Button(text="Start installer", width=25, height=5, bg="#2467a0", command=startupins)
startup = tk.Button(text="Start mod manager", width=25, height=5, bg="#2467a0")
greeting.pack()
startupins.pack()
startup.pack()

window.mainloop()