import tkinter as tk
from tkinter import messagebox
import sys

def show_error(error_message):
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    messagebox.showerror("Error", error_message)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python err.pyw <error_message>")
        sys.exit(1)
    
    error_message = " ".join(sys.argv[1:])
    show_error(error_message)
