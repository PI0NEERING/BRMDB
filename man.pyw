import tkinter as tk
import subprocess
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
modpath = os.path.join(current_dir, "mods")
modlist_path = os.path.join(current_dir, "modlist.txt")

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def open_directory():
    os.startfile(modpath)  # Open the selected directory

def delete_mod(mod_name):
    mod_exe = os.path.join(modpath, f"{mod_name}.exe")
    if os.path.exists(mod_exe):
        os.remove(mod_exe)
    with open(modlist_path, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if mod_name not in line:
                file.write(line)
        file.truncate()
    refresh_modlist_text()

def refresh_modlist_text():
    modlist_text.config(state=tk.NORMAL)
    modlist_text.delete('1.0', tk.END)
    if os.path.exists(modlist_path):
        with open(modlist_path, 'r') as file:
            modlist_contents = file.read()
        modlist_text.insert(tk.END, modlist_contents)
    else:
        modlist_text.insert(tk.END, "Mod list not found")
    modlist_text.config(state=tk.DISABLED)

window = tk.Tk()
window.title("Mod Manager")  # Set the title of the window
window.configure(bg='#34A2FE')

greeting = tk.Label(window, text="Manage Mods", background="#34A2FE", font=('Arial', 25), pady=20)
open_button = tk.Button(window, text="Open Mod Directory", width=25, height=2, bg="#2467a0", fg="white", font=('Arial', 12, 'bold'), command=open_directory)
modlist_label = tk.Label(window, text="Mod List:", font=('Arial', 20))

modlist_text = tk.Text(window, height=10, width=50, font=('Arial', 12))
modlist_text.config(state=tk.DISABLED)  # Make the text widget read-only

# Read the contents of modlist.txt
refresh_modlist_text()

greeting.pack()
open_button.pack(pady=10)
modlist_label.pack()
modlist_text.pack(pady=5)

# Add delete buttons next to each mod in the mod list
with open(modlist_path, 'r') as file:
    for mod_name in file:
        mod_name = mod_name.strip()  # Remove leading/trailing whitespace
        delete_button = tk.Button(window, text=f"Delete {mod_name}", bg="#2467a0", fg="white", font=('Arial', 10, 'bold'), command=lambda name=mod_name: delete_mod(name))
        delete_button.pack()

window.mainloop()