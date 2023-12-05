import requests
import tkinter as tk
from tkinter import scrolledtext

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
