import re
import tkinter as tk
from tkinter import messagebox
import requests
import os
import subprocess
import sys

# Function to download file
def download_file(url, filename):
    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
        print(f"File downloaded successfully from {url} to {filename}")
    except requests.RequestException as e:
        messagebox.showerror("Error", f"Failed to download file: {e}")

# Function to search and download file
def search_and_download():
    keyword = entry.get().strip()
    print(f"Keyword: {keyword}")
    mdb_url = "https://brmdb.vercel.app/mdb.txt"
    
    try:
        # Fetch data from mdb.txt
        response = requests.get(mdb_url)
        response.raise_for_status()
        mdb_data = response.text
        
        # Find keyword in mdb.txt and get the corresponding value
        keyword_line = None
        for line in mdb_data.split('\n'):
            if line.startswith(keyword + '='):
                keyword_line = line
                break
        if keyword_line is None:
            messagebox.showinfo("Info", f"No match found for '{keyword}' in mdb.txt.")
            return

        # Extract URL enclosed within double quotes
        download_link = re.search(r'"(.*?)"', keyword_line)
        if download_link:
            download_link = download_link.group(1)
            download_file(download_link, 'temp.xdelta')
            apply_patch(keyword)
            add_to_modlist(keyword)
        else:
            messagebox.showerror("Error", f"No valid download link found for '{keyword}'.")

    except requests.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch data: {e}")

# Function to apply patch
def apply_patch(keyword):
    try:
        # Make a copy of Buckshot Roulette.exe as br.exe
        source_file = r"C:\Program Files (x86)\Steam\steamapps\common\Buckshot Roulette\Buckshot Roulette_windows\Buckshot Roulette.exe"
        
        # Apply the patch to br.exe
        patch_file = "temp.xdelta"
        destination_mod_file = os.path.join("mods", f"{keyword}.exe")
        process = subprocess.Popen(["xdelta3.exe", "-f", "-d", "-s", source_file, patch_file, destination_mod_file])

    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to apply patch: {e}")

# Function to add entry to modlist.txt if mod exists
def add_to_modlist(keyword):
    mod_file_path = os.path.join("mods", f"{keyword}.exe")
    try:
        with open('modlist.txt', 'r+') as f:
            modlist_content = f.read()
            if keyword not in modlist_content:
                f.write(keyword + '\n')
                print(f"Added '{keyword}' to modlist.txt")
            else:
                print(f"'{keyword}' already exists in modlist.txt")
    except IOError as e:
        messagebox.showerror("Error", f"Failed to write to modlist.txt: {e}")

# Create Tkinter window
window = tk.Tk()
window.title("BRMDB Patch Downloader")

# Create search label and entry
search_label = tk.Label(window, text="Enter keyword:", font=('Arial', 15))
search_label.pack()
entry = tk.Entry(window)
entry.pack()

# Create search button
search_button = tk.Button(window, text="Search and Download", command=search_and_download)
search_button.pack()

# Run the Tkinter event loop
window.mainloop()
