import tkinter as tk
from tkinter import ttk


def translate():
 print('translate')
# Create the main window
window = tk.Tk()
window.title('Test No.1')
window.geometry('300x200')  # Adjusted height for additional text

green = '#8ACE00'

# Title
title_label = tk.Label(master=window, text='German to English flash cards', font='Calibri 24 bold', background=green)
title_label.pack(pady=10)  # Added padding for better spacing

# Subtitle/Text below the title
subtitle_label = ttk.Label(master=window, text='Translate this: Danke', font='Calibri 14')
subtitle_label.pack(pady=5)  # Added padding for better spacing

# Input field
input_frame = ttk.Frame(master=window)
entry = ttk.Entry(master=input_frame)
button = ttk.Button(master=input_frame, text='Check answer', command = translate)

def check_answer():
    user_input = entry.get()
    # You can implement your answer checking logic here
    print(f'User input: {user_input}')  # Placeholder action

# Assign the function to the button (NEW LINE)
button.config(command=check_answer)

# Pack the widgets
entry.pack()
button.pack()
input_frame.pack(pady=20)  # Added padding for the input frame

# Run the application
window.mainloop()