# Importing The Necessary Modules ---

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  
import requests

# Function to fetch meaning from the Dictionary API

def get_meaning():
    word = entry_word.get().lower()
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data:
            meanings = data[0]["meanings"][0]["definitions"][0]["definition"]
            label_meaning.config(text=f"Meaning: {meanings}")
        else:
            label_meaning.config(text="No meaning found.")
    else:
        messagebox.showerror("Error", "Word not found!")

# Initializing Tkinter window

window = tk.Tk()
window.title("Enhanced Dictionary")
window.geometry("500x400")
window.config(bg="#f5f5f5")

# Loading and display logo image

try:
    logo_img = Image.open("C://Users//DELL//Desktop//Dict//dict.png")  
    logo_img = logo_img.resize((100, 100), Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(logo_img)
    logo_label = tk.Label(window, image=logo, bg="#f5f5f5")
    logo_label.pack(pady=10)
except Exception as e:
    print("Logo image not found.")

# Title Label

title_label = tk.Label(window, text="Dictionary", font=("Arial", 24, "bold"), bg="#f5f5f5", fg="#333333")
title_label.pack(pady=5)

# Input for word

label_word = tk.Label(window, text="Enter Word:", font=("Arial", 14), bg="#f5f5f5", fg="#333333")
label_word.pack(pady=10)
entry_word = tk.Entry(window, font=("Arial", 14), width=30, bd=2, relief="solid")
entry_word.pack()

# Search button 

button_search = tk.Button(window, text="Search", command=get_meaning, font=("Arial", 12), bg="#4CAF50", fg="white", bd=0, padx=20, pady=5)
button_search.pack(pady=15)

# Label to display meanings with updated style

label_meaning = tk.Label(window, text="Meaning:", font=("Arial", 12), wraplength=400, bg="#f5f5f5", fg="#333333", justify="left")
label_meaning.pack(pady=10)

# Running the Tkinter main loop

window.mainloop()