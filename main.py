import requests
import tkinter as tk
from tkinter import scrolledtext

def get_atc_info(member_id):
    url = f"https://api.vatsim.net/v2/members/{member_id}/atc"
    payload = {}
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers, data=payload)
    return response.text

def show_atc_info():
    member_id = member_id_entry.get()
    atc_info = get_atc_info(member_id)
    output_text.delete(1.0, tk.END)  # Clear previous text
    output_text.insert(tk.END, atc_info)

# Create the main window
window = tk.Tk()
window.title("VATSIM ATC Info")

# Create an entry widget for the member ID
member_id_label = tk.Label(window, text="Member ID:")
member_id_label.pack(pady=5)
member_id_entry = tk.Entry(window)
member_id_entry.pack(pady=5)

# Create a button to fetch and display ATC information
fetch_button = tk.Button(window, text="Fetch ATC Info", command=show_atc_info)
fetch_button.pack(pady=10)

# Create a scrolled text widget to display the output
output_text = scrolledtext.ScrolledText(window, width=50, height=20)
output_text.pack(padx=10, pady=10)

# Run the Tkinter event loop
window.mainloop()
