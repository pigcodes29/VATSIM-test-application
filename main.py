import requests
import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk

def get_atc_info(member_id):
    url = f"https://api.vatsim.net/v2/members/{member_id}/atc"
    payload = {}
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers, data=payload)
    return response.json()

def format_atc_info(atc_data):
    formatted_info = ""
    if "items" in atc_data:
        for item in atc_data["items"]:
            formatted_info += f"Connection ID: {item['connection_id']['id']}\n"
            formatted_info += f"Callsign: {item['connection_id']['callsign']}\n"
            formatted_info += f"Start: {item['connection_id']['start']}\n"
            formatted_info += f"End: {item['connection_id']['end']}\n"
            formatted_info += "--------------------------\n"
    else:
        formatted_info = "No ATC information found."

    return formatted_info

def show_atc_info():
    member_id = member_id_entry.get()
    atc_info = get_atc_info(member_id)
    formatted_info = format_atc_info(atc_info)
    output_text.delete(1.0, tk.END)  # Clear previous text
    output_text.insert(tk.END, formatted_info)

# Create the main window
window = tk.Tk()
window.title("VATSIM ATC Info")

# Load the image using Pillow and convert it to PhotoImage
img = Image.open("bdl.jpg")

# Resize the image to a smaller size while maintaining the aspect ratio
max_size = (100, 100)
img.thumbnail(max_size)

img = ImageTk.PhotoImage(img)

img_label = tk.Label(window, image=img)

# Place the image in the top right corner
img_label.place(relx=1, x=-10, rely=0, y=10, anchor="ne")

# Create an entry widget for the member ID
member_id_label = tk.Label(window, text="Member ID:")
member_id_label.pack(pady=5)
member_id_entry = tk.Entry(window)
member_id_entry.pack(pady=5)

# Create a button to fetch and display ATC information
fetch_button = tk.Button(window, text="Fetch ATC Info", command=show_atc_info)
fetch_button.pack(pady=10)

# Create a scrolled text widget to display the output
output_text = scrolledtext.ScrolledText(window, width=80, height=20)
output_text.pack(padx=10, pady=10)

# Run the Tkinter event loop
window.mainloop()
