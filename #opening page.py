#opening page

import tkinter as tk
from tkinter import OptionMenu


window = tk.Tk()
window.title('German Flash Cards')
window.geometry('550x410')
window.config(bg = 'CadetBlue1')

#label
label = tk.Label(master = window, text = 'Home Page', 
        bg = 'CadetBlue4',
        fg = 'CadetBlue3',
        font = ('Helvetica', 20))
label.pack(pady = 20)

drop = OptionMenu(window, 'Common B1 Vocabulary', 'Gender Guessing Exercise', 'Colours')
drop.pack() 


#TTK BUTTON
button = tk.Button(master = window, text = 'button',
        bg = 'red',
        fg = 'black',
        font = ('Arial', 10))
button.pack(pady = 80)

#run
window.mainloop()