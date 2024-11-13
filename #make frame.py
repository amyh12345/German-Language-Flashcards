import tkinter as tk

window = tk.Tk()
window.title('German Flash Cards')
window.geometry('600x600')

# make frame
main_frame = tk.Frame(window)
main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

def basicvocab_page():
    basicvocab_frame = tk.Frame(main_frame)
    lb = tk.Label(basicvocab_frame, text= 'Basic Vocab', font= ('Bold', 30))
    basicvocab_frame.pack(pady=20)

def gender_page():
    gender_frame = tk.Frame(main_frame)
    lb = tk.Label(gender_frame, text= 'Gender', font= ('Bold', 30))
    gender_frame.pack(pady=20)

def colour_page():
    colour_frame = tk.Frame(main_frame)
    lb = tk.Label(colour_frame, text= 'colour ', font= ('Bold', 30))
    colour_frame.pack(pady=20)

options_frame = tk.Frame(window, bg = '#c3c3c3')

basicvocab_btn = tk.Button(options_frame, text='B1 Random Vocab', font=('Bold', 15),
                           fg= 'red', bd= 0, wraplength=150, padx=10, pady=10)
basicvocab_btn.place(x=10, y=50)

gender_btn = tk.Button(options_frame, text='Guess the gender', font=('Bold', 15),
                           fg= 'red', bd= 0, wraplength=150, padx=10, pady=10)
gender_btn.place(x=10, y=100)

colour_btn = tk.Button(options_frame, text='Colours', font=('Bold', 15),
                           fg= 'red', bd= 0, wraplength=150, padx=10, pady=10)
colour_btn.place(x=10, y=150)

# ensures the bar is on left side
options_frame.pack(side=tk.LEFT)
# if you write 'False', you can set frame item width
options_frame.pack_propagate(False)
options_frame.configure(width=200, height=600)

# Creating main frame with border highlighting
main_frame = tk.Frame(window, highlightbackground= 'black', highlightthickness=2)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(width=600, height=600)

window.mainloop()
